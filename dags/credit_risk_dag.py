from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    'credit_risk_etl',
    start_date=datetime(2026, 8, 23),
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    extract = BashOperator(
        task_id='extract',
        bash_command='python extract.py'
    )
    
    transform_load = BashOperator(
        task_id='transform_load',
        bash_command='python transform_load.py'
    )
    
    extract >> transform_load