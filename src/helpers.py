import datetime
import logging
import sys
import time
import yaml
from pathlib import Path
from sqlalchemy import create_engine, exc as sqlalchemy_exc
from sqlalchemy.engine.base import Engine
from typing import Any, Union


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
