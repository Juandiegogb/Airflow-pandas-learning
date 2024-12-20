from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator


TAGS = ["testing"]
DAG_ID = "mi primeras dag"
DAG_DESCRIPTION = "Este es un test"
DAG_SCHEDULE = "*/15 * * * *"
retries = 4
retry_delay = timedelta(minutes=5)


def execute_task():
    print("Hola mundo")


dag = DAG(dag_id=DAG_ID, catchup=False, schedule_interval=DAG_SCHEDULE)
