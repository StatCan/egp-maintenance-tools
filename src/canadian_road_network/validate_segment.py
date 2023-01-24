import click
import geopandas as gpd
import logging
import math
import pandas as pd
import sys
import uuid
from copy import deepcopy
from itertools import tee
from math import atan2, cos, dist, radians, sin
from operator import attrgetter, itemgetter
from pathlib import Path
from shapely.geometry import LineString, MultiPoint
from shapely.ops import polygonize, unary_union
from tabulate import tabulate
from typing import List, Tuple

filepath = Path(__file__).resolve()
sys.path.insert(1, str(Path(__file__).resolve().parents[1]))
import helpers

# Set logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)


class DatasetValidation:
    """Validates a dataset."""

    def __init__(self, url: str, schema: str = "public", geom_col: str = "geom") -> None:
        """
        Class initialization.

        \b
        :param str url: database URL. General format: postgresql://[user[:password]@][netloc][:port][/dbname]
        :param str schema: database schema, default=public.
        :param str geom_col: geometry column for spatial datasets, default=geom.
        """

        self.dataset = "segment"
        self.id = "segment_id"
        self.dataset_meshblock = "basic_block"
        self.id_meshblock = "bb_uid"
        self.id_meshblock_left = "bb_uid_l"
        self.id_meshblock_right = "bb_uid_r"
        self.id_meshblock_parent = "cb_uid"

        logger.info(f"Initializing dataset validation for: {self.dataset}.")

        self.url = url
        self.schema = schema
        self.geom_col = geom_col

        # Define outputs.
        self.errors = dict()
        self.export = dict()

        # Create database engine.
        self.engine = helpers.create_db_engine(self.url)

        # Define validations.
        self.validations = {
            101: self.construction_zero_length,
            102: self.construction_simple,
            103: self.construction_cluster_tolerance,
            201: self.duplication_duplicated,
            202: self.duplication_overlap,
            301: self.connectivity_node_intersection,
            302: self.connectivity_segmentation,
            401: self.meshblock_count,
            402: self.meshblock_boundary,
        }

        # Define validation thresholds.
        self._min_vertex_dist = 0.01

        # Load datasets.
        dfs = helpers.load_db_datasets(self.engine, subset=[self.dataset, self.dataset_meshblock], schema=self.schema,
                                       geom_col=self.geom_col)

        # Load dataset - Arcs.
        self.df = dfs[self.dataset].copy(deep=True)
        self.df.index = self.df[self.id]

        # Load dataset - Meshblock.
        self.meshblock_existing = dfs[self.dataset_meshblock].copy(deep=True)
        self.meshblock_existing.index = self.meshblock_existing[self.id_meshblock]

        # Generate reusable geometry variables.
        self._gen_reusable_variables()

    def __call__(self) -> None:
        """Executes the class."""

        self._validate()
        self._write_errors()

        # Update meshblock only if no errors remain on the primary arc dataset.
        if not any(map(len, self.errors.values())):
            self._update_meshblock()
            self._write_meshblock_updates()

    def _configure_meshblock_parity(self, pts: Tuple[tuple, ...], indexes: Tuple[int, ...]) -> Tuple[int, int]:
        """
        Returns the indexes of the meshblock polygons which are formed by the left and right sides of a LineString. The
        process creates a LineString from the first point to halfway towards the second point and then, alternating
        between the left and right sides, creates rotated LineStrings at decreasing angles until only 1 meshblock
        polygon covers the LineString. This method accounts for complex meshblock polygons which may be formed by one
        side of the LineString but wrap around to occupy space on the other side as well.

        \b
        :param Tuple[tuple, ...] pts: Tuple coordinate sequence extracted from a LineString.
        :param Tuple[int, ...] indexes: Positional indexes of meshblock polygons which cover the LineString.
        :return Tuple[int, int]: Positional index of left and right side meshblock polygons, in that order.
        """

        # Calculate angle (theta) and half distance of current vector.
        pt1, pt2 = itemgetter(0, 1)(pts)
        distance = dist(pt1, pt2) / 2
        theta = atan2((itemgetter(1)(pt2) - itemgetter(1)(pt1)), (itemgetter(0)(pt2) - itemgetter(0)(pt1)))
        if theta < 0:
            theta += radians(360)

        # Compile meshblock polygons associated with each index. Add null key for 1-sided arcs.
        polys_lookup = {idx: itemgetter(idx)(self.meshblock_idx_geom_lookup) for idx in indexes}

        # Iteratively rotate vector by decreasing angles starting from 1 degrees.
        # Alternate between left (positive angle) and right (negative angle) sides to account for 1-sided arcs.
        rotation = radians(1)
        covers = [False, False]

        while sum(covers) != 1:

            # Rotate geometry.
            g_rotated = LineString([pt1, (itemgetter(0)(pt1) + (distance * cos(theta + rotation)),
                                          itemgetter(1)(pt1) + (distance * sin(theta + rotation)))])

            # Test for covering polygons.
            covers = [poly.covers(g_rotated) for idx, poly in polys_lookup.items()]

            # Change sign of rotation angle for next iteration.
            rotation = (rotation / 2) * -1

        # Assign polygon indexes to left and right sides based on rotation sign.
        # Assign index of -1 for side of 1-sided arcs without a meshblock polygon.
        # Note: Since rotation sign is changed at the end of each iteration, the parity and signs are opposite (i.e.
        #       positive sign = right, negative sign = left).
        idx = itemgetter(covers.index(True))(list(polys_lookup))
        idx_opposite = -1 if (len(indexes) == 1) else itemgetter(covers.index(False))(list(polys_lookup))
        if rotation < 0:
            return idx, idx_opposite
        else:
            return idx_opposite, idx

    def _gen_reusable_variables(self) -> None:
        """Generates reusable geometry attributes."""

        logger.info("Generating reusable geometry attributes.")

        # Generate vertex attributes as new columns.
        self.df["pts_tuple"] = self.df[self.geom_col].map(attrgetter("coords")).map(tuple)
        self.df["pt_start"] = self.df["pts_tuple"].map(itemgetter(0))
        self.df["pt_end"] = self.df["pts_tuple"].map(itemgetter(-1))
        self.df["pts_ordered_pairs"] = self.df["pts_tuple"].map(self._ordered_pairs)

        # Generate meshblock.
        self.meshblock = gpd.GeoDataFrame(geometry=list(polygonize(unary_union(self.df[self.geom_col].to_list()))),
                                          crs=self.df.crs)

        # Generate meshblock attributes as new columns.
        self.df["meshblock_covered_by"] = self.df[self.geom_col].map(
            lambda g: tuple(self.meshblock.sindex.query(g, predicate="covered_by")))
        meshblock_boundaries = self.meshblock.boundary
        self.df["meshblock_boundary_covered_by"] = self.df[self.geom_col].map(
            lambda g: tuple(meshblock_boundaries.sindex.query(g, predicate="covered_by")))

        # Generate placeholder variable for to-be-generated meshblock index and geometry lookup.
        self.meshblock_idx_geom_lookup = dict()

        # Generate existing meshblock identifier and geometry lookups.
        self.meshblock_existing_id_parent_id_lookup = dict(zip(self.meshblock_existing[self.id_meshblock],
                                                               self.meshblock_existing[self.id_meshblock_parent]))
        self.meshblock_existing_geom_id_lookup = dict(zip(self.meshblock_existing[self.geom_col].to_wkt(),
                                                          self.meshblock_existing[self.id_meshblock]))

        # Generate existing meshblock parent geometry and identifier lookup.
        meshblock_existing_dissolve = self.meshblock_existing.dissolve(by=self.id_meshblock_parent, as_index=False)
        self.meshblock_existing_parent_geom_id_lookup = dict(zip(meshblock_existing_dissolve[self.geom_col].to_wkt(),
                                                                 meshblock_existing_dissolve[self.id_meshblock_parent]))

    @staticmethod
    def _ordered_pairs(coords: Tuple[tuple, ...]) -> List[Tuple[tuple, tuple]]:
        """
        Creates an ordered sequence of adjacent coordinate pairs, sorted.

        \b
        :param Tuple[tuple, ...] coords: tuple of coordinate tuples.
        :return List[Tuple[tuple, tuple]]: ordered sequence of coordinate pair tuples.
        """

        coords_1, coords_2 = tee(coords)
        next(coords_2, None)

        return sorted(zip(coords_1, coords_2))

    def _update_meshblock(self) -> None:
        f"""
        Updates meshblock dataset based on changes to the underlying arc dataset and repairs their attribute 
        linkages.
        """

        logger.info(f"Updating meshblock dataset: {self.dataset_meshblock}.")

        # Meshblock - Restore unique identifiers. For non-matches, generate a new identifier.
        self.meshblock[self.id_meshblock] = self.meshblock[self.geom_col].to_wkt()\
            .map(self.meshblock_existing_geom_id_lookup)\
            .fillna(dict(zip(self.meshblock.index, [uuid.uuid4() for _ in range(len(self.meshblock))])))

        # Meshblock - Restore parent unique identifiers. Populate non-matches with the Nil UUID.
        self.meshblock[self.id_meshblock_parent] = self.meshblock[self.id_meshblock]\
            .map(self.meshblock_existing_id_parent_id_lookup).fillna(uuid.UUID(int=0))

        # Meshblock - Assign the Nil UUID to all parent unique identifiers where any constituent meshblock polygons
        # failed to match.
        meshblock_dissolve = self.meshblock.dissolve(by=self.id_meshblock_parent, as_index=False)
        meshblock_invalid_parent_ids = set(meshblock_dissolve.loc[
            meshblock_dissolve[self.geom_col].to_wkt().map(self.meshblock_existing_parent_geom_id_lookup).isna(),
            self.id_meshblock_parent
        ])
        self.meshblock.loc[self.meshblock[self.id_meshblock_parent].isin(meshblock_invalid_parent_ids),
                           self.id_meshblock_parent] = uuid.UUID(int=0)

        # Arcs - Populate left and right-side meshblock identifiers.

        # Classify arcs according to the amount of meshblock polygons they form (covered_by boundary results).
        flag_contained = self.df["meshblock_boundary_covered_by"].map(len) == 0
        flag_not_contained = self.df["meshblock_boundary_covered_by"].map(len) > 0

        # Generate meshblock index, identifier, and geometry lookups.
        meshblock_idx_id_lookup = dict(zip(range(len(self.meshblock)), self.meshblock[self.id_meshblock]))
        meshblock_idx_id_lookup[-1] = uuid.UUID(int=0)
        self.meshblock_idx_geom_lookup = dict(zip(range(len(self.meshblock)), self.meshblock[self.geom_col]))

        # Arc scenario: contained - Populate meshblock identifiers based on single result of non-boundary covered_by.
        self.df.loc[flag_contained, self.id_meshblock_left] = self.df.loc[flag_contained, "meshblock_covered_by"]\
            .map(lambda idxs: meshblock_idx_id_lookup[itemgetter(0)(idxs)])
        self.df.loc[flag_contained, self.id_meshblock_right] = self.df.loc[flag_contained, self.id_meshblock_left]

        # Arc scenario: not contained - Pass points tuple and meshblock covered_by indexes to configuration function.
        df_not_contained = self.df.loc[flag_not_contained].copy(deep=True)
        df_not_contained["_args"] = df_not_contained[["pts_tuple", "meshblock_covered_by"]].apply(
            lambda row: (row[0], row[1]), axis=1)
        df_not_contained["_results"] = df_not_contained["_args"].map(
            lambda args: self._configure_meshblock_parity(*args))

        # Arc scenario: not contained - Assign parity results (indexes) as meshblock identifiers.
        self.df.loc[df_not_contained.index, self.id_meshblock_left] = df_not_contained["_results"].map(
            lambda idx: meshblock_idx_id_lookup[itemgetter(0)(idx)])
        self.df.loc[df_not_contained.index, self.id_meshblock_right] = df_not_contained["_results"].map(
            lambda idx: meshblock_idx_id_lookup[itemgetter(-1)(idx)])

    def _validate(self) -> None:
        """Executes validations."""

        logger.info("Applying validations.")

        # Iterate validations.
        for code, func in self.validations.items():
            logger.info(f"Applying validation {code}: {func.__name__}.")

            try:

                # Execute validation and store results.
                self.errors[code] = deepcopy(func())

            except (KeyError, SyntaxError, ValueError) as e:
                logger.exception(f"Unable to apply validation {code}: {func.__name__}. Exception details:\n"
                                 f"{type(e).__name__}: {e}", exc_info=False)
                sys.exit(1)

    def _write_errors(self) -> None:
        """Write validation error flags to dataset as integer columns."""

        logger.info(f"Writing error flags to dataset: {self.schema}.{self.dataset}.")

        # Iterate validation results.
        statements = list()
        for code, vals in sorted(self.errors.items()):

            # Create SQL statement to drop pre-existing column.
            statements.append(f"ALTER TABLE {self.schema}.{self.dataset} DROP COLUMN IF EXISTS v{code};")

            if len(vals):

                # Create SQL statement to add and populate new column for invalid records.
                statements.append(f"""
                ALTER TABLE {self.schema}.{self.dataset} ADD COLUMN v{code} INTEGER DEFAULT 0;
                UPDATE {self.schema}.{self.dataset} SET v{code} = 1 WHERE {self.id} IN {*vals,};
                """)

        # Execute statements.
        helpers.execute_db_statements(engine=self.engine, statements=tuple(statements))

        # Log validation results summary.
        summary = tabulate(
            [[f"{code} ({self.validations[code].__name__})", len(vals)] for code, vals in sorted(self.errors.items())],
            headers=["Validation", "Invalid Count"], tablefmt="rst", colalign=("left", "right"))

        logger.info("Validation results:\n" + summary)

    def _write_meshblock_updates(self) -> None:
        f"""Write meshblock updates to datasets {self.dataset_meshblock} and {self.dataset}."""

        logger.info(f"Writing meshblock updates to dataset: {self.schema}.{self.dataset_meshblock} and underlying "
                    f"dataset: {self.schema}.{self.dataset}.")

        statements = dict()

        # Compile meshblock updates.
        meshblock_added = set(self.meshblock[self.id_meshblock]) - set(self.meshblock_existing[self.id_meshblock])
        meshblock_removed = set(self.meshblock_existing[self.id_meshblock]) - set(self.meshblock[self.id_meshblock])

        # Create SQL statements for added meshblock records.
        if len(meshblock_added):

            values = self.meshblock.loc[self.meshblock[self.id_meshblock].isin(meshblock_added),
                                        [self.id_meshblock, self.id_meshblock_parent, self.geom_col]]\
                .apply(lambda row: f"({itemgetter(0)(row)}, {itemgetter(1)(row)}, {itemgetter(2)(row)})", axis=1)

            statements["meshblock_added"] = f"""
            INSERT INTO {self.schema}.{self.dataset_meshblock} ({self.id_meshblock}, {self.id_meshblock_parent}, 
            {self.geom_col}) VALUES {', '.join(values)};
            """

        # Create SQL statements for removed meshblock records.
        if len(meshblock_removed):

            statements["meshblock_removed"] = f"""
            DELETE FROM {self.schema}.{self.dataset_meshblock} WHERE {self.id_meshblock} IN {*meshblock_removed,};
            """

        # Compile arc-meshblock identifier updates.
        meshblock_left_lookup = dict(zip(self.df[self.id], self.df[self.id_meshblock_left]))
        meshblock_right_lookup = dict(zip(self.df[self.id], self.df[self.id_meshblock_right]))
        df_updated = self.df.loc[
            (self.df[self.id_meshblock_left] != self.df[self.id].map(meshblock_left_lookup)) |
            (self.df[self.id_meshblock_right] != self.df[self.id].map(meshblock_right_lookup))].copy(deep=True)

        # Create SQL statements for arc-meshblock identifier updates.
        if len(df_updated):

            values = df_updated[[self.id, self.id_meshblock_left, self.id_meshblock_right]].apply(
                lambda row: f"{itemgetter(0, 1, 2)(row)}", axis=1)

            statements["arcs_modified"] = (
                f"""
                CREATE TABLE {self.schema}._ ({self.id} uuid, {self.id_meshblock_left} uuid, {self.id_meshblock_right} 
                uuid);
                """,
                f"""
                INSERT INTO {self.schema}._ ({self.id}, {self.id_meshblock_left}, {self.id_meshblock_right}) VALUES 
                {', '.join(values)};
                """,
                f"""
                UPDATE {self.schema}.{self.dataset} AS dst SET {self.id_meshblock_left} = src.{self.id_meshblock_left} 
                FROM {self.schema}._ AS src WHERE dst.{self.id} = src.{self.id};
                """,
                f"""
                UPDATE {self.schema}.{self.dataset} AS dst SET {self.id_meshblock_right} = src.{self.id_meshblock_right} 
                FROM {self.schema}._ AS src WHERE dst.{self.id} = src.{self.id};
                """,
                f"""
                DROP TABLE {self.schema}._;
                """
            )

        # Execute statements.
        for update_type in [k for k in ("meshblock_added", "arcs_modified", "meshblock_removed") if k in statements]:
            helpers.execute_db_statements(engine=self.engine, statements=statements[update_type])

        # Log meshblock updates.
        summary = tabulate([["Added", len(meshblock_added)],
                            ["Removed", len(meshblock_removed)],
                            ["Unchanged", len(self.meshblock) - len(meshblock_added) - len(meshblock_removed)]],
                           headers=["Status", "Count"], tablefmt="rst", colalign=("left", "right"))
        logger.info(f"Meshblock ({self.dataset_meshblock}) updates:\n" + summary)

        # Log arc-meshblock identifier updates.
        summary = tabulate([["Modified", len(df_updated)],
                            ["Unchanged", len(self.df) - len(df_updated)]],
                           headers=["Status", "Count"], tablefmt="rst", colalign=("left", "right"))
        logger.info(f"Arc-meshblock identifier ({self.dataset}.{self.id_meshblock_left}/{self.id_meshblock_right}) "
                    f"updates:\n" + summary)

    def connectivity_node_intersection(self) -> set:
        """
        Validates: Arcs must only connect at endpoints (nodes).

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Compile nodes.
        nodes = set(pd.concat([self.df["pt_start"], self.df["pt_end"]]))

        # Compile interior vertices (non-nodes).
        # Note: only arcs with > 2 vertices are used.
        non_nodes = set(self.df.loc[self.df["pts_tuple"].map(len) > 2, "pts_tuple"]
                        .map(lambda pts: set(pts[1:-1])).explode())

        # Compile invalid vertices.
        invalid_pts = nodes.intersection(non_nodes)
        if len(invalid_pts):

            # Filter arcs to those with an invalid vertex as a node.
            flag = self.df.loc[(self.df["pt_start"].isin(invalid_pts)) | (self.df["pt_end"].isin(invalid_pts))]

            # Compile errors.
            if sum(flag):
                errors.update(set(self.df.loc[flag].index))

        return errors

    def connectivity_segmentation(self) -> set:
        """
        Validates: Arcs must not cross (i.e. must be segmented at each intersection).

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Query arcs which cross each arc.
        crosses = self.df[self.geom_col].map(lambda g: set(self.df.sindex.query(g, predicate="crosses")))

        # Flag arcs which have one or more crossing arcs.
        flag = crosses.map(len) > 0

        # Compile errors.
        if sum(flag):
            errors.update(set(self.df.loc[flag].index))

        return errors

    def construction_cluster_tolerance(self) -> set:
        """
        Validates: Arcs must have >= 0.01 meters distance between adjacent vertices (cluster tolerance).

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Filter arcs to those with > 2 vertices.
        df = self.df.loc[self.df["pts_tuple"].map(len) > 2]
        if len(df):

            # Explode arc coordinate pairs and calculate distances.
            coord_pairs = df["pts_ordered_pairs"].explode()
            coord_dist = coord_pairs.map(lambda pair: math.dist(*pair))

            # Flag pairs with distances that are too small.
            flag = coord_dist < self._min_vertex_dist

            # Compile errors.
            if sum(flag):
                errors.update(set(coord_pairs.loc[flag].index))

                # Export invalid pairs as MultiPoint geometries.
                pts = coord_pairs.loc[flag].map(MultiPoint)
                pts_df = gpd.GeoDataFrame({self.id: pts.index.values}, geometry=[*pts], crs=self.df.crs)
                self.export[f"reference_cluster_tolerance"] = pts_df.copy(deep=True)

        return errors

    def construction_simple(self) -> set:
        """
        Validates: Arcs must be simple (i.e. must not self-overlap, self-cross, nor touch their interior).

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Flag complex (non-simple) geometries.
        flag = ~self.df.is_simple

        # Compile errors.
        if sum(flag):
            errors.update(set(self.df.loc[flag].index))

        return errors

    def construction_zero_length(self) -> set:
        """
        Validates: Arcs must not have zero length.

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Flag arcs with zero length.
        flag = self.df.length == 0

        # Compile errors.
        if sum(flag):
            errors.update(set(self.df.loc[flag].index))

        return errors

    def duplication_duplicated(self) -> set:
        """
        Validates: Arcs must not be duplicated.

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Filter arcs to those with duplicated lengths.
        df = self.df.loc[self.df.length.duplicated(keep=False)]
        if len(df):

            # Filter arcs to those with duplicated nodes.
            df = df.loc[df[["pt_start", "pt_end"]].agg(set, axis=1).map(tuple).duplicated(keep=False)]

            # Flag duplicated geometries.
            duplicates = df.loc[
                df[self.geom_col].map(lambda g1: df[self.geom_col].map(lambda g2: g1.equals(g2)).sum() > 1)]

            # Compile errors.
            if len(duplicates):
                errors.update(set(duplicates.index))

        return errors

    def duplication_overlap(self) -> set:
        """
        Validates: Arcs must not overlap (i.e. contain duplicated adjacent vertices).

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Query arcs which overlap each arc.
        overlaps = self.df[self.geom_col].map(lambda g: set(self.df.sindex.query(g, predicate="overlaps")))

        # Flag arcs which have one or more overlapping arcs.
        flag = overlaps.map(len) > 0

        # Compile errors.
        if sum(flag):
            errors.update(set(overlaps.loc[flag].index))

        return errors

    def meshblock_boundary(self) -> set:
        """
        Validates: Boundary arcs must form a meshblock polygon.

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Flag boundary arcs which do not form a meshblock polygon.
        flag = (self.df["segment_type"] == 2) & (self.df["meshblock_boundary_covered_by"].map(len) == 0)

        # Compile error logs.
        if sum(flag):
            errors.update(set(self.df.loc[flag].index))

        return errors

    def meshblock_count(self) -> set:
        """
        Validates: Arcs must be covered by only 1 or 2 meshblock polygons.

        \b
        :return set: set containing identifiers of erroneous records.
        """

        errors = set()

        # Flag arcs which form an invalid amount of meshblock polygons.
        flag = ~self.df["meshblock_covered_by"].map(len).between(1, 2, inclusive=True)

        # Compile error logs.
        if sum(flag):
            errors.update(set(self.df.loc[flag].index))

        return errors


@click.command()
@click.argument("url", type=click.STRING)
@click.option("--schema", default="public", show_default=True, help="Database schema.")
@click.option("--geom_col", default="geom", show_default=True, help="Geometry column for spatial datasets.")
def main(url: str, schema: str = "public", geom_col: str = "geom") -> None:
    """
    Validates dataset: segment.

    URL: Database URL. General format: postgresql://[user[:password]@][netloc][:port][/dbname]

    \f\b
    :param str url: database URL. General format: postgresql://[user[:password]@][netloc][:port][/dbname]
    :param str schema: database schema, default=public.
    :param str geom_col: geometry column for spatial datasets, default=geom.
    """

    try:

        with helpers.Timer():
            validation = DatasetValidation(url, schema, geom_col)
            validation()

    except Exception as e:
        logger.exception(f"Unhandled exception encountered. Exception details:\n{type(e).__name__}: {e}",
                         exc_info=False)
        sys.exit(1)


if __name__ == "__main__":
    main()
