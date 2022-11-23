import click
import geopandas as gpd
import logging
import pandas as pd
import sys
from pathlib import Path
from sqlalchemy import exc as sqlalchemy_exc, inspect
from typing import Union

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


class DataModelValidation:
    """Validates a data model."""

    def __init__(self, model: str, db_url: str, db_schema: Union[str, None]) -> None:
        """
        Class initialization.

        \b
        :param str model: name of the data model to be validated.
        :param str db_url: database connection URL.
        :param Union[str, None] db_schema: database schema.
        """

        logger.info(f"Initializing data model validation for: {model}.")

        self.model = model
        self.db_url = db_url
        self.db_schema = db_schema
        self.geom_col = "geom"

        # Create database connection.
        self.db_con = helpers.create_db_connection(self.db_url)

        # Configure default schema.
        self.db_inspection = inspect(self.db_con)
        if not self.db_schema:
            self.db_schema = self.db_inspection.default_schema_name

        # Compile configuration files.
        path_constraints = Path(self.model, "constraints.yaml").resolve()
        path_domains = Path(self.model, "domains.yaml").resolve()
        self.constraints = helpers.load_yaml(path_constraints) if path_constraints.exists() else dict()
        self.domains = helpers.load_yaml(path_domains) if path_domains.exists() else dict()

        # Configure datasets in data model.
        self.datasets = set(self.db_inspection.get_table_names()).intersection(set(self.constraints.keys())
                                                                               .union(set(self.domains.keys())))
        self.dfs = dict()

        # Define validations.
        self.validations = {
            101: self.existence_exists,
            201: self.domains_domain,
            301: self.constraints_nullable,
            302: self.constraints_unique,
            303: self.constraints_dtype,
            304: self.constraints_foreign_keys,
        }

    def __call__(self) -> None:
        """Executes the class."""

        self._load_datasets()
        self._validate()
        self._write_errors()

    def _load_datasets(self) -> None:
        """Loads all data model datasets."""

        logger.info(f"Loading datasets.")

        # Load datasets.
        for dataset in self.datasets:

            try:

                logger.info(f"Loading dataset: {dataset}.")

                # Define query.
                query = f"select * from {self.db_schema}.{dataset}"

                # Spatial.
                if self.geom_col in self.db_con.execute(f"{query} limit 0").keys():
                    self.dfs[dataset] = gpd.read_postgis(query, con=self.db_con).copy(deep=True)

                # Tabular.
                else:
                    self.dfs[dataset] = pd.read_sql(query, con=self.db_con).copy(deep=True)

                logger.info(f"Successfully loaded {len(self.dfs[dataset])} records from {self.db_schema}.{dataset}.")

            except (sqlalchemy_exc.SQLAlchemyError, TypeError, ValueError):
                logger.exception(f"Failed to load dataset: {self.db_schema}.{dataset}.")

    def _validate(self) -> None:
        ...

    def _write_errors(self) -> None:
        ...

    def constraints_dtype(self) -> set:
        ...

    def constraints_foreign_keys(self) -> set:
        ...

    def constraints_nullable(self) -> set:
        ...

    def constraints_unique(self) -> set:
        ...

    def domains_domain(self) -> set:
        ...

    def existence_exists(self) -> set:
        ...


@click.command()
@click.argument("model", type=click.Choice(sorted(set(map(lambda f: f.parent.stem, Path().glob("**/*.yaml")))), False))
@click.argument("db_url", type=click.STRING,
                help="General format: postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]")
@click.option("--db_schema", help="Database schema. Will detect and use the default schema if none is provided.")
def main(model: str, db_url: str, db_schema: Union[str, None]) -> None:
    """
    Validates a data model.

    \b
    :param str model: name of the data model to be validated.
    :param str db_url: database connection URL.
    :param Union[str, None] db_schema: database schema.
    """

    try:

        with helpers.Timer():
            validation = DataModelValidation(model, db_url, db_schema)
            validation()

    except KeyboardInterrupt:
        logger.exception("KeyboardInterrupt: Exiting program.")
        sys.exit(1)


if __name__ == "__main__":
    main()
