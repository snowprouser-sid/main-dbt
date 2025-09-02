from pathlib import Path
from dagster_dbt import DbtProject

# Corrected path: This should point to the root of your dbt project
# (the folder that contains dbt_project.yml, models/, etc.)
snowflake_python_workshop_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..").resolve(), # Now points to C:\Users\thath\dbt-proj\main-dbt\
)