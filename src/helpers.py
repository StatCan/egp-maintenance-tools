import datetime
import geopandas as gpd
import logging
import pandas as pd
import sys
import time
import yaml
from pathlib import Path
from sqlalchemy import create_engine, exc, inspect, text
from sqlalchemy.engine.base import Engine
from typing import Any, Dict, Sequence, Tuple, Union


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


def create_db_engine(url: str) -> Engine:
    """
    Creates a database engine based on a database URL.

    \b
    :param str url: database URL.
    :return sqlalchemy.engine.base.Engine: database engine.
    """

    logger.info(f"Creating database engine: {url}.")

    try:

        # Create database engine.
        engine = create_engine(url)

        # Test database connection.
        _ = inspect(engine)

    except exc.SQLAlchemyError as e:
        logger.exception(f"Unable to create database engine. Exception details:\n{type(e).__name__}: {e}",
                         exc_info=False)
        sys.exit(1)

    return engine


def execute_db_statements(engine: Engine, statements: Union[str, Tuple[str, ...]]) -> None:
    """
    Executes one or more SQL statements as a database transaction.

    \b
    :param sqlalchemy.engine.base.Engine engine: database engine.
    :param Union[str, Tuple[str, ...]] statements: SQl statement or sequence of statements to be executed.
    """

    logger.info("Executing SQL statements.")

    # Resolve statement inputs.
    if isinstance(statements, str):
        statements = (statements,)

    # Run and commit transaction.
    try:

        with engine.begin() as con:

            # Iterate statements.
            for statement in statements:
                _ = con.execute(text(statement.replace(",)", ")")))

    except exc.SQLAlchemyError as e:
        logger.exception(f"Unable to execute SQL statement. Exception details:\n{type(e).__name__}: {e}",
                         exc_info=False)
        sys.exit(1)


def load_db_datasets(engine: Engine, subset: Sequence[str] = None, schema: str = "public", geom_col: str = "geom") -> \
        Dict[str, Union[gpd.GeoDataFrame, pd.DataFrame]]:
    """
    Loads all or a specified subset of datasets from a given database.

    \b
    :param sqlalchemy.engine.base.Engine engine: database engine.
    :param Sequence[str] subset: sequence of dataset names, default=None.
    :param str schema: database schema, default=public.
    :param str geom_col: geometry column for spatial datasets, default=geom.
    :return Dict[str, Union[gpd.GeoDataFrame, pd.DataFrame]]: dictionary of dataset names and (Geo)DataFrames.
    """

    logger.info("Loading datasets.")

    dfs = dict()

    # Configure existing and requested datasets.
    datasets = set(inspect(engine).get_table_names())
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
            if geom_col in engine.execute(f"{query} limit 0").keys():
                dfs[dataset] = gpd.read_postgis(query, con=engine).copy(deep=True)

            # Tabular.
            else:
                dfs[dataset] = pd.read_sql(query, con=engine).copy(deep=True)

            logger.info(f"Successfully loaded {len(dfs[dataset])} records from {schema}.{dataset}.")

        except (exc.SQLAlchemyError, TypeError, ValueError) as e:
            logger.exception(f"Failed to load dataset: {schema}.{dataset}. Exception details:\n{type(e).__name__}: {e}",
                             exc_info=False)
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

        except (ValueError, yaml.YAMLError) as e:
            logger.exception(f"Unable to load yaml: {path}. Exception details:\n{type(e).__name__}: {e}",
                             exc_info=False)
            sys.exit(1)
