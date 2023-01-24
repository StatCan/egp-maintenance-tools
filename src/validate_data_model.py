# TODO: Modify this script to compile and execute all individual validation scripts within the directory of the given data model.
#       The only question mark is how to handle validation scripts with different inputs.

import click
import helpers
import logging
import sys
from pathlib import Path

# Set logger.
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S"))
logger.addHandler(handler)


class DataModelValidation:
    """Validates a data model."""

    def __init__(self, model: str, url: str, schema: str = "public", geom_col: str = "geom") -> None:
        """
        Class initialization.

        \b
        :param str model: name of the data model to be validated.
        :param str url: database URL.
        :param str schema: database schema, default=public.
        :param str geom_col: geometry column for spatial datasets, default=geom.
        """

        logger.info(f"Initializing data model validation for: {model}.")

        self.model = model
        self.url = url
        self.schema = schema
        self.geom_col = geom_col
        self.dfs = dict()

        # Create database engine.
        self.engine = helpers.create_db_engine(self.url)

        # Define validations.
        self.validations = {
            #TODO - may not be needed.
        }

    def __call__(self) -> None:
        """Executes the class."""

        self.dfs = helpers.load_db_datasets(self.engine, schema=self.schema, geom_col=self.geom_col)
        self._validate()
        self._write_errors()

    def _validate(self) -> None:
        ...

    def _write_errors(self) -> None:
        ...


@click.command()
@click.argument("model", type=click.Choice(sorted(set(map(lambda f: f.parent.stem, Path().glob("**/*.yaml")))), False))
@click.argument("url", type=click.STRING,
                help="General format: postgresql://[user[:password]@][netloc][:port][/dbname]")
@click.option("--schema", default="public", show_default=True,
              help="Database schema. Will detect and use the default schema if none is provided.")
@click.option("--geom_col", default="geom", show_default=True, help="Geometry column for spatial datasets.")
def main(model: str, url: str, schema: str = "public", geom_col: str = "geom") -> None:
    """
    Validates a data model.

    \b
    :param str model: name of the data model to be validated.
    :param str url: database URL.
    :param str schema: database schema, default=public.
    :param str geom_col: geometry column for spatial datasets, default=geom.
    """

    try:

        with helpers.Timer():
            validation = DataModelValidation(model, url, schema, geom_col)
            validation()

    except Exception as e:
        logger.exception(f"Unhandled exception encountered. Exception details:\n{type(e).__name__}: {e}",
                         exc_info=False)
        sys.exit(1)


if __name__ == "__main__":
    main()
