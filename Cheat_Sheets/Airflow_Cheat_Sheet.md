# Apache Airflow Cheat Sheet

## Core Concepts

| Term | Description |
|--------|------------|
| DAG | Directed Acyclic Graph |
| Task | Individual unit of work |
| Operator | Defines task behavior |
| Scheduler | Determines when tasks run |
| Worker | Executes tasks |
| Executor | Controls task execution |
| Trigger | Starts DAG execution |

---

## Common Imports

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
```

---

## DAG Template

```python
with DAG(
    "example_dag",
    start_date=days_ago(1),
    schedule_interval="@daily",
    catchup=False
) as dag:
```

---

## Python Task

```python
task = PythonOperator(
    task_id="task_name",
    python_callable=my_function
)
```

---

## Bash Task

```python
task = BashOperator(
    task_id="install_package",
    bash_command="pip install package"
)
```

---

## Task Dependencies

```python
t1 >> t2 >> t3
```

---

## Common Commands

```bash
docker compose up -d
docker compose down
docker ps
airflow dags list
airflow tasks list
```