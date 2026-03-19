from airflow.decorators import dag, task
from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2026, 1, 1),
    tags=["aws"],
)
def s3_dag():
    wait_for_file = S3KeySensor(
        task_id="wait_for_file",
        bucket_key="s3://astro-test-bucket-1376/data_*",
        aws_conn_id="aws_s3",
        wildcard_match=True,
    )

    @task
    def process_file():
        print("File is available, processing...")

    wait_for_file >> process_file()

s3_dag_instance = s3_dag()