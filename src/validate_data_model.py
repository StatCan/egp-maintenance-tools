# TODO: data model validations may not be needed at all since all domains and constraints, including defaults can be managed by postgresql.
#       Perhaps adding the contents of domains.yaml and constraints.yaml to the data model draw.io file (on separate tabs) is sufficient.
#       Only dataset specific tools are required (e.g. validate_segment.py, validate_crossing.py, validate_basic_block.py).

import click
import logging
import sys
from pathlib import Path

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

    def __init__(self, model: str, url: str, schema: str = "public", geom_col: str = "geometry") -> None:
        """
        Class initialization.

        \b
        :param str model: name of the data model to be validated.
        :param str url: database connection URL.
        :param str schema: database schema, default=public.
        :param str geom_col: geometry column for spatial datasets, default=geometry.
        """

        logger.info(f"Initializing data model validation for: {model}.")

        self.model = model
        self.url = url
        self.schema = schema
        self.geom_col = geom_col
        self.dfs = dict()

        # Create database connection.
        self.con = helpers.create_db_connection(self.url)

        # Compile configuration files.
        path_constraints = Path(self.model, "constraints.yaml").resolve()
        path_domains = Path(self.model, "domains.yaml").resolve()
        self.constraints = helpers.load_yaml(path_constraints) if path_constraints.exists() else dict()
        self.domains = helpers.load_yaml(path_domains) if path_domains.exists() else dict()

        # Define validations.
        self.validations = {
            110: self.existence_exists,
            210: self.domains_domain,
            310: self.constraints_nullable,
            320: self.constraints_unique,
            330: self.constraints_dtype,
            340: self.constraints_default,
            350: self.constraints_foreign_keys
        }

    def __call__(self) -> None:
        """Executes the class."""

        self.dfs = helpers.load_db_datasets(self.con,
                                            subset=list(set(self.constraints.keys()).union(set(self.domains.keys()))),
                                            schema=self.schema, geom_col=self.geom_col)
        self._validate()
        self._write_errors()

    def _validate(self) -> None:
        ...

    def _write_errors(self) -> None:
        ...

    def constraints_default(self) -> set:
        """
        Validation: Data type.

        \b
        :return set: set containing unique identifiers of erroneous records.
        """

        errors = set()

        # Placeholder validation. Constraint managed by PostgreSQL.

        return errors

    def constraints_dtype(self) -> set:
        """
        Validation: Data type.

        \b
        :return set: set containing unique identifiers of erroneous records.
        """

        errors = set()

        # Placeholder validation. Constraint managed by PostgreSQL.

        return errors

    def constraints_foreign_keys(self) -> set:
        """
        Validation: Data type.

        \b
        :return set: set containing unique identifiers of erroneous records.
        """

        errors = set()

        # Placeholder validation. Constraint managed by PostgreSQL.

        return errors

    def constraints_nullable(self) -> set:
        """
        Validation: Data type.

        \b
        :return set: set containing unique identifiers of erroneous records.
        """

        errors = set()

        # Placeholder validation. Constraint managed by PostgreSQL.

        return errors

    def constraints_unique(self) -> set:
        """
        Validation: Data type.

        \b
        :return set: set containing unique identifiers of erroneous records.
        """

        errors = set()

        # Placeholder validation. Constraint managed by PostgreSQL.

        return errors

    def domains_domain(self) -> set:
        """
        Validation: Data type.

        \b
        :return set: set containing unique identifiers of erroneous records.
        """

        errors = set()

        # Placeholder validation. Constraint managed by PostgreSQL.

        return errors

    def existence_exists(self) -> set:
        ...


@click.command()
@click.argument("model", type=click.Choice(sorted(set(map(lambda f: f.parent.stem, Path().glob("**/*.yaml")))), False))
@click.argument("url", type=click.STRING,
                help="General format: postgresql://[user[:password]@][netloc][:port][/dbname]")
@click.option("--schema", default="public", show_default=True,
              help="Database schema. Will detect and use the default schema if none is provided.")
@click.option("--geom_col", default="geometry", show_default=True, help="Geometry column for spatial datasets.")
def main(model: str, url: str, schema: str = "public", geom_col: str = "geometry") -> None:
    """
    Validates a data model.

    \b
    :param str model: name of the data model to be validated.
    :param str url: database connection URL.
    :param str schema: database schema, default=public.
    :param str geom_col: geometry column for spatial datasets, default=geometry.
    """

    try:

        with helpers.Timer():
            validation = DataModelValidation(model, url, schema, geom_col)
            validation()

    except KeyboardInterrupt:
        logger.exception("KeyboardInterrupt: Exiting program.")
        sys.exit(1)


if __name__ == "__main__":
    main()
