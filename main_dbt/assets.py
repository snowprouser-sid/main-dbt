from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import snowflake_python_workshop_project


@dbt_assets(manifest=snowflake_python_workshop_project.manifest_path)
def snowflake_python_workshop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

