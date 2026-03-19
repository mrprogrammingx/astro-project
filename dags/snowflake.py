from airflow.sdk import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


@dag
def snowflake():
    run_query = SQLExecuteQueryOperator(
        task_id="run_query",
        conn_id="snowflake_conn",
        sql="SELECT CURRENT_VERSION()",
    )
    
snowflake_instance = snowflake()
