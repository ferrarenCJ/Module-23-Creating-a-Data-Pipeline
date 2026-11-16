# Apache Airflow Notes

## Overview

Apache Airflow is an open-source workflow orchestration platform used to automate, schedule, and monitor data pipelines.

In Module 23, Airflow was used to orchestrate the Sensemaking Data Pipeline that extracted, processed, analyzed, and visualized MIT course catalog data.

---

# Key Concepts

## DAG (Directed Acyclic Graph)

A DAG defines the workflow and ordering of tasks.

Example:

```text
task_zero
      ↓
task_one
      ↓
task_two
      ↓
task_three
      ↓
task_four
      ↓
task_five
```

---

## Operators

Operators define the work performed by a task.

### BashOperator

Executes shell commands.

Example:

```python
BashOperator(
    task_id='task_zero',
    bash_command='pip install beautifulsoup4'
)
```

### PythonOperator

Executes Python functions.

Example:

```python
PythonOperator(
    task_id='task_one',
    python_callable=catalog
)
```

---

## Scheduler

The scheduler manages task execution and determines when tasks should run.

---

## Worker

Workers execute tasks assigned by the scheduler.

---

## Airflow Workflow Used in Project 23.1

```text
catalog()
     ↓
combine()
     ↓
titles()
     ↓
clean()
     ↓
count_words()
```

---

# Useful Commands

## Start Airflow

```bash
docker compose up -d
```

## Stop Airflow

```bash
docker compose down
```

## View Containers

```bash
docker ps
```

## View Logs

```bash
docker logs airflow-docker-airflow-worker-1
```

## Enter Container

```bash
docker exec -it airflow-docker-airflow-worker-1 bash
```

---

# Lessons Learned

- Airflow tasks should be small and focused.
- DAGs simplify workflow automation.
- Logs are critical when troubleshooting task failures.
- Docker provides a reproducible Airflow environment.