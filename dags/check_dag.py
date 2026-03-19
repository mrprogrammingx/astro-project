from airflow.sdk import dag, task
from pendulum import datetime

@dag(
    schedule="@daily",
    start_date=datetime(2025, 1, 1),
    description="DAG to check data",
)

def check_dag():
    @task.bash
    def create_file():
        return 'echo "Hi there!" >/tmp/dummy'
    
    @task.bash
    def check_file():
        return 'test -f /tmp/dummy'

    @task.bash
    def read_file():
        print(open('/tmp/dummy', 'rb').read())
        return 'cat /tmp/dummy'

    @task.bash
    def delete_file():
        return 'rm /tmp/dummy'

    create_file() >> check_file() >> read_file() >> delete_file()


check_dag_instance = check_dag()