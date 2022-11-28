import click
import geopandas as gpd
import logging
import pandas as pd
import sys
from pathlib import Path

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
        logger.info(f"Initializing dataset validation for: {self.dataset}.")

        self.url = url
        self.schema = schema
        self.geom_col = geom_col

        # Create database connection.
        self.con = helpers.create_db_connection(self.url)

        # Define validations.
        self.validations = {
            ...
        }

    def __call__(self) -> None:
        """Executes the class."""

        self.df = helpers.load_db_datasets(self.con, subset=[self.dataset], schema=self.schema, geom_col=self.geom_col)
        self._validate()
        self._write_errors()

    def _validate(self) -> None:
        ...

    def _write_errors(self) -> None:
        ...

    def placeholder_validation(self) -> set:
        """
        Validation: Data type.

        \b
        :return set: set containing unique identifiers of erroneous records.
        """

        errors = set()

        # Placeholder validation.

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
