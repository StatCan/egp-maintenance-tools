import datetime
import geopandas as gpd
import logging
import pandas as pd
import sys
import time
import yaml
from pathlib import Path
from sqlalchemy import create_engine, exc as sqlalchemy_exc, inspect
from sqlalchemy.engine.base import Engine
from typing import Any, Dict, List, Union


# Set logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)


class Timer:
    """Tracks stage runtime."""

    def __init__(self) -> None:
        """Initializes the Timer class."""

        self.start_time = None

    def __enter__(self) -> None:
        """Starts the timer."""

        logger.info("Started.")
        self.start_time = time.time()

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        """
        Computes and returns the elapsed time.

        \b
        :param Any exc_type: required parameter for __exit__.
        :param Any exc_val: required parameter for __exit__.
        :param Any exc_tb: required parameter for __exit__.
        """

        total_seconds = time.time() - self.start_time
        delta = datetime.timedelta(seconds=total_seconds)
        logger.info(f"Finished. Time elapsed: {delta}.")


def create_db_connection(url: str) -> Engine:
    """
    Connects to a database based on a connection URL.

    \b
    :param str url: database connection URL.
    :return sqlalchemy.engine.base.Engine: database connection.
    """

    logger.info(f"Creating database connection: {url}.")

    # Create database engine.
    try:

        con = create_engine(url)

    except sqlalchemy_exc.SQLAlchemyError as e:
        logger.exception(f"Unable to create database connection: {url}.")
        logger.exception(e)
        sys.exit(1)

    return con


def load_db_datasets(con: Engine, subset: List[str] = None, schema: str = "public", geom_col: str = "geometry") -> \
        Dict[str, Union[gpd.GeoDataFrame, pd.DataFrame]]:
    """
    Loads all or a specified subset of datasets from a given database.

    \b
    :param sqlalchemy.engine.base.Engine con: database connection.
    :param List[str] subset: list of dataset names, default=None.
    :param str schema: database schema, default=public.
    :param str geom_col: geometry column for spatial datasets, default=geometry.
    :return Dict[str, Union[gpd.GeoDataFrame, pd.DataFrame]]: dictionary of dataset names and (Geo)DataFrames.
    """

    logger.info("Loading datasets.")

    dfs = dict()

    # Configure existing and requested datasets.
    datasets = set(inspect(con).get_table_names())
    if subset:
        datasets = datasets.intersection(subset)

        # Log invalid subset.
        invalid = set(subset).difference(datasets)
        if len(invalid):
            logger.exception(f"Invalid dataset(s) provided: {*invalid,}.".replace(",)", ")"))
            sys.exit(1)

    # Load datasets.
    for dataset in datasets:

        try:

            logger.info(f"Loading dataset: {dataset}.")

            # Define query.
            query = f"select * from {schema}.{dataset}"

            # Spatial.
            if geom_col in con.execute(f"{query} limit 0").keys():
                dfs[dataset] = gpd.read_postgis(query, con=con).copy(deep=True)

            # Tabular.
            else:
                dfs[dataset] = pd.read_sql(query, con=con).copy(deep=True)

            logger.info(f"Successfully loaded {len(dfs[dataset])} records from {schema}.{dataset}.")

        except (sqlalchemy_exc.SQLAlchemyError, TypeError, ValueError):
            logger.exception(f"Failed to load dataset: {schema}.{dataset}.")
            sys.exit(1)

    return dfs


def load_yaml(path: Union[Path, str]) -> Any:
    """
    Loads the content of a YAML file as a Python object.

    \b
    :param Union[Path, str] path: path to the YAML file.
    :return Any: Python object consisting of the YAML content.
    """

    path = Path(path).resolve()

    with open(path, "r", encoding="utf8") as f:

        try:

            return yaml.safe_load(f)

        except (ValueError, yaml.YAMLError):
            logger.exception(f"Unable to load yaml: {path}.")
