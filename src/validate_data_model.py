import click
import geopandas as gpd
import logging
import pandas as pd
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

    def __init__(self, model: str) -> None:
        """
        Class initialization.

        \b
        :param str model: name of the data model to be validated.
        """

        logger.info("Initializing class.")

        self.model = model

        # Define validations.
        # Note: List validations in order if execution order matters.
        self.validations = {}

    def __call__(self) -> None:
        """Executes the class."""

        # TODO add helpers.py with timer function - add to imports at top.

        # TODO: load datasets (could be in init)
        # TODO: dataset existence
        # TODO: constraints and domains validations
        # TODO: log results.


@click.command()
@click.argument("model", type=click.Choice(map(str, filter(lambda f: f.is_dir(), Path().iterdir())), False))
def main(model: str) -> None:
    """
    Instantiates and executes the class.

    \b
    :param str model: name of the data model to be validated.
    """

    try:

        with helpers.Timer():
            validation = DataModelValidation(model)
            validation()

    except KeyboardInterrupt:
        logger.exception("KeyboardInterrupt: Exiting program.")
        sys.exit(1)


if __name__ == "__main__":
    main()