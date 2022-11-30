import click
import geopandas as gpd
import logging
import math
import pandas as pd
import sys
from itertools import tee
from operator import attrgetter, itemgetter
from pathlib import Path
from shapely.geometry import MultiPoint
from typing import List, Tuple

filepath = Path(__file__).resolve()
sys.path.insert(1, str(Path(__file__).resolve().parents[2]))
import helpers

# Set logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)


class SegmentValidation:
    """Validates dataset: segment."""

    def __init__(self, url: str, schema: str = "public", geom_col: str = "geometry") -> None:
        """
        Class initialization.

        \b
        :param str url: database connection URL.
        :param str schema: database schema, default=public.
        :param str geom_col: geometry column for spatial datasets, default=geometry.
        """

        self.dataset = "segment"
        self.id = "segment_id"
        logger.info(f"Initializing dataset validation for: {self.dataset}.")

        self.url = url
        self.schema = schema
        self.geom_col = geom_col

        # Define outputs.
        self.errors = dict()
        self.export = dict()

        # Create database connection.
        self.con = helpers.create_db_connection(self.url)

        # Generate reusable geometry variables.
        self._gen_reusable_variables()

        # Define validations.
        self.validations = {
            101: self.construction_zero_length,
            102: self.construction_simple,
            103: self.construction_cluster_tolerance,
            201: self.duplication_duplicated,
            202: self.duplication_overlap,
            301: self.connectivity_node_intersection,
            302: self.connectivity_segmentation,
            400: ...meshblock validations
        }

        # Define validation thresholds.
        self._min_vertex_dist = 0.01

    def __call__(self) -> None:
        """Executes the class."""

        # Load data, exclude ferries.
        self.df = helpers.load_db_datasets(self.con, subset=[self.dataset], schema=self.schema, geom_col=self.geom_col)
        self.df.index = self.df[self.id]
        self.df = self.df.loc[self.df["segment_type"] != 2].copy(deep=True)

        self._validate()
        self._write_errors()

    def _gen_reusable_variables(self) -> None:
        """Generates computationally intensive, reusable geometry attributes."""

        logger.info("Generating reusable geometry attributes.")

        # Generate computationally intensive geometry attributes as new columns.
        self.df["pts_tuple"] = self.df["geometry"].map(attrgetter("coords")).map(tuple)
        self.df["pt_start"] = self.df["pts_tuple"].map(itemgetter(0))
        self.df["pt_end"] = self.df["pts_tuple"].map(itemgetter(-1))
        self.df["pts_ordered_pairs"] = self.df["pts_tuple"].map(self._ordered_pairs)

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

    def _validate(self) -> None:
        ...

    def _write_errors(self) -> None:
        # TODO: write errors and export required outputs to working schema.
        # TODO: add logic to clear existing output datasets.

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
        crosses = self.df["geometry"].map(lambda g: set(self.df.sindex.query(g, predicate="crosses")))

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
                self.export[f"validation_construction_cluster_tolerance"] = pts_df.copy(deep=True)

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
            duplicates = df.loc[df["geometry"].map(lambda g1: df["geometry"].map(lambda g2: g1.equals(g2)).sum() > 1)]

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
        overlaps = self.df["geometry"].map(lambda g: set(self.df.sindex.query(g, predicate="overlaps")))

        # Flag arcs which have one or more overlapping arcs.
        flag = overlaps.map(len) > 0

        # Compile errors.
        if sum(flag):
            errors.update(set(overlaps.loc[flag].index))

        return errors


@click.command()
@click.argument("url", type=click.STRING,
                help="General format: postgresql://[user[:password]@][netloc][:port][/dbname]")
@click.option("--schema", default="public", show_default=True,
              help="Database schema. Will detect and use the default schema if none is provided.")
@click.option("--geom_col", default="geometry", show_default=True, help="Geometry column for spatial datasets.")
def main(url: str, schema: str = "public", geom_col: str = "geometry") -> None:
    """
    Validates dataset: segment.

    \b
    :param str url: database connection URL.
    :param str schema: database schema, default=public.
    :param str geom_col: geometry column for spatial datasets, default=geometry.
    """

    try:

        with helpers.Timer():
            validation = SegmentValidation(url, schema, geom_col)
            validation()

    except KeyboardInterrupt:
        logger.exception("KeyboardInterrupt: Exiting program.")
        sys.exit(1)


if __name__ == "__main__":
    main()
