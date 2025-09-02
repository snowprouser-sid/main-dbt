from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import snowflake_python_workshop_dbt_assets
from .project import snowflake_python_workshop_project
from .schedules import schedules

defs = Definitions(
    assets=[snowflake_python_workshop_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=snowflake_python_workshop_project),
    },
)

