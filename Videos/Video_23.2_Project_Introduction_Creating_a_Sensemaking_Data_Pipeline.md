# Video 23.2: Project Introduction: Creating a Sensemaking Data Pipeline

**Duration:** 00:56

---

## Overview

In this video, Dr. Sanchez introduces the objectives and workflow of **Project 23.1: Creating a Sensemaking Data Pipeline**.

The primary goal of the project is to transform unstructured MIT course catalog data into structured, meaningful information through the development of an automated data pipeline.

The project emphasizes the concept of **sensemaking**, which involves extracting useful insights from raw, unstructured data and organizing it into a format that can be analyzed and visualized.

---

## Project Goal

Create an end-to-end data pipeline that can:

1. Extract unstructured course catalog data.
2. Process and clean the data.
3. Transform the data into a structured format.
4. Analyze the resulting dataset.
5. Produce meaningful insights.
6. Execute the entire workflow automatically with minimal or no human intervention.

---

## Workflow Architecture

The project breaks the overall process into **10 discrete tasks**.

Rather than manually running each step, the workflow will be automated using **Apache Airflow**.

```text
Unstructured MIT Course Catalog Data
                │
                ▼
        Task 1 - Extraction
                │
                ▼
        Task 2 - Cleaning
                │
                ▼
        Task 3 - Transformation
                │
               ...
                │
                ▼
       Additional Processing Tasks
                │
                ▼
         Data Analysis
                │
                ▼
        Visualization Output
```

---

## Apache Airflow's Role

Airflow serves as the workflow orchestration platform for the project.

### Responsibilities

- Automate task execution
- Manage task dependencies
- Schedule workflow execution
- Monitor pipeline progress
- Ensure tasks run in the proper sequence

By defining each step as an Airflow task, the pipeline can execute from start to finish automatically.

---

## Key Concept: Automation

A major objective of the project is achieving full workflow automation.

### Manual Process

```text
Human executes Task 1
Human executes Task 2
Human executes Task 3
...
Human executes Task 10
```

### Automated Process

```text
Airflow executes Task 1
        │
        ▼
Airflow executes Task 2
        │
        ▼
Airflow executes Task 3
        │
       ...
        │
        ▼
Airflow executes Task 10
```

The desired outcome is a pipeline that can process and analyze data **without requiring human intervention between steps**.

---

## Key Takeaways

- The project focuses on creating a **Sensemaking Data Pipeline**.
- Unstructured MIT course catalog data serves as the data source.
- The project workflow is divided into **10 independent tasks**.
- Apache Airflow will orchestrate and automate task execution.
- The end goal is an automated pipeline capable of extracting, transforming, analyzing, and visualizing data.
- Automation reduces manual effort and improves the repeatability of data processing workflows.

---

## Personal Notes

### Data Engineering Perspective

This project mirrors a real-world ETL/ELT workflow:

```text
Extract
    ↓
Transform
    ↓
Analyze
    ↓
Visualize
```

Key technologies introduced:

- Python
- Apache Airflow
- Docker
- JSON
- D3.js
- Data Pipelines
- Workflow Orchestration

### Why This Matters

This is one of the first projects in the MIT program that combines:

- Data acquisition
- Data transformation
- Workflow orchestration
- Automation
- Visualization

into a single end-to-end solution.

The final deliverable closely resembles how modern data engineering pipelines are built in production environments.