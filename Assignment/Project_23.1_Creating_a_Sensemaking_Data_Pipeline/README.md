# Required Project 23.1: Creating a Sensemaking Data Pipeline

## Project Information

| Item | Details |
|--------|----------|
| Module | Module 23 - Creating a Data Pipeline |
| Project | Project 23.1 |
| Points | 100 |
| Due Date | Thursday, November 19, 2026 at 4:29 PM UTC |
| Submission Type | Word Document with Screenshots |
| Estimated Time | 10 Hours |

---

# Learning Outcomes

By completing this project, you will be able to:

1. Implement JavaScript tools to visualize word frequency data.
2. Create a sensemaking data pipeline.

---

# Project Overview

In this project, you will create an automated data pipeline that extracts unstructured data from the MIT Course Catalog, transforms it into a structured dataset, and visualizes the results using D3.js.

The project combines:

- Python
- HTML
- JSON
- BeautifulSoup
- Apache Airflow
- Docker
- JavaScript
- D3.js

into a complete end-to-end data engineering workflow.

---

# Project Architecture

```text
MIT Course Catalog
         │
         ▼
Data Extraction
(urllib)
         │
         ▼
Raw HTML Files
         │
         ▼
Combine HTML Files
         │
         ▼
Extract Course Titles
(BeautifulSoup)
         │
         ▼
Clean Words
         │
         ▼
Count Word Frequency
         │
         ▼
words.json
         │
         ▼
D3 Visualization
         │
         ▼
Bubble Chart
```

---

# Technologies Used

## Data Extraction

- urllib

## Data Processing

- BeautifulSoup4
- JSON
- Python

## Workflow Orchestration

- Apache Airflow

## Containerization

- Docker

## Visualization

- JavaScript
- D3.js

---

# Deliverables

The final submission is a Word document containing screenshots that demonstrate:

1. Project setup
2. Python task implementation
3. Airflow DAG configuration
4. Docker execution
5. Generated JSON files
6. D3 visualizations

---

# Part 1: Code Development

---

## Step 1: Create Project Structure

### Required Folder Structure

```text
project-23
│
├── airflow-docker
│
├── code_visualization
│
└── assignment.py
```

### Deliverable

Screenshot showing:

- project-23 folder
- airflow-docker folder
- code_visualization folder
- assignment.py

---

## Step 2: Import Required Libraries

### Required Imports

```python
from airflow import DAG
from datetime import timedelta
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator

import urllib.request
import time
import glob
import os
import json
```

### Deliverable

Screenshot showing all required imports.

---

## Step 3: Build Task 1 - catalog()

### Purpose

Download MIT Course Catalog HTML pages.

### Helper Functions

#### pull(url)

Responsible for:

```text
Retrieve HTML content
```

#### store(data, file)

Responsible for:

```text
Store HTML content locally
```

### Expected Workflow

```text
URL
 ▼
pull()
 ▼
HTML Data
 ▼
store()
 ▼
HTML File
```

### Deliverable

Screenshot showing:

- catalog()
- pull()
- store()

---

## Step 4: Build URL Processing Loop

### Purpose

Iterate through all URLs.

### Workflow

```python
for url in urls:
```

Each iteration:

1. Calls pull()
2. Creates filename
3. Calls store()
4. Waits 15 seconds

### Deliverable

Screenshot showing:

- urls list
- for loop
- pull()
- store()

---

## Step 5: Build Task 2 - combine()

### Purpose

Combine downloaded HTML files into a single file.

### Output

```text
combo.txt
```

### Workflow

```text
HTML Files
      ▼
combine()
      ▼
combo.txt
```

### Deliverable

Screenshot showing complete combine() function.

---

## Step 6: Build Task 3 - titles()

### Purpose

Extract course titles from HTML.

### Library

```python
BeautifulSoup4
```

### Processing Steps

1. Read combo.txt
2. Parse HTML
3. Find all h3 tags
4. Extract text
5. Save JSON

### Output

```text
titles.json
```

### Deliverable

Screenshot showing completed titles() method.

---

## Step 7: Build Task 4 - clean()

### Purpose

Clean extracted course titles.

### Actions

Remove:

- Punctuation
- Numbers
- Single-character words

### Output

```text
titles_clean.json
```

### Deliverable

Screenshot showing completed clean() method.

---

## Step 8: Build Task 5 - count_words()

### Purpose

Calculate word frequencies.

### Library

```python
collections.Counter
```

### Processing

```text
titles_clean.json
         ▼
Extract Words
         ▼
Count Frequencies
         ▼
words.json
```

### Output

```text
words.json
```

### Deliverable

Screenshot showing completed count_words() function.

---

## Step 9: Create Airflow DAG

### Required Tasks

| Task | Function |
|--------|----------|
| t0 | Install BeautifulSoup |
| t1 | catalog() |
| t2 | combine() |
| t3 | titles() |
| t4 | clean() |
| t5 | count_words() |

### Workflow

```text
t0
 ▼
t1
 ▼
t2
 ▼
t3
 ▼
t4
 ▼
t5
```

### Deliverable

Screenshot showing DAG definition and all tasks.

---

# Part 2: Code Execution

---

## Step 10: Deploy to Airflow

### Copy DAG

```bash
cp assignment.py airflow-docker/dags
```

### Configure Docker

Increase:

- CPU
- Memory

### Install Airflow

Follow Mini-Lesson 19.2.

### Deliverable

Screenshot showing Airflow containers running in Docker.

---

## Step 11: Execute DAG

### Access Airflow

```text
http://localhost:8080
```

### Credentials

```text
Username: airflow
Password: airflow
```

Run:

```text
assignment DAG
```

### Deliverable

Screenshot showing successful DAG execution.

---

## Step 12: Retrieve words.json

### Access Worker Container

```bash
docker exec -it airflow-docker-airflow-worker-1 /bin/bash
```

### Confirm File Exists

```bash
ls
```

Verify:

```text
words.json
```

### Copy File to Local Machine

```bash
docker cp airflow-docker-airflow-worker-1:/opt/airflow/words.json YOUR_PATH_HERE
```

### Create words.js

Transfer contents from:

```text
words.json
```

to:

```text
words.js
```

### Deliverable

Screenshot showing beginning of words.js.

---

## Step 13: Run Provided Visualization

### Open

```text
mitcourses_graph.html
```

Example:

```text
file:///YOUR_PATH/project-23/code_visualization/mitcourses_graph.html
```

### Deliverable

Screenshot showing visualization output.

---

## Step 14: Create Enhanced D3 Visualization

### Objective

Modify:

```text
d3_bubble_chart_example.html
```

to visualize:

```text
words.json
```

### Example Bubble Visualization

```text
Large Bubble
      Data

Medium Bubble
      Systems

Small Bubble
      Engineering
```

### Deliverable

Screenshot showing enhanced D3 visualization.

---

# Submission Checklist

## Part 1: Code Development

- [ ] Step 1 Screenshot
- [ ] Step 2 Screenshot
- [ ] Step 3 Screenshot
- [ ] Step 4 Screenshot
- [ ] Step 5 Screenshot
- [ ] Step 6 Screenshot
- [ ] Step 7 Screenshot
- [ ] Step 8 Screenshot
- [ ] Step 9 Screenshot

## Part 2: Code Execution

- [ ] Docker Running Screenshot
- [ ] Successful DAG Screenshot
- [ ] words.js Screenshot
- [ ] D3 Visualization Screenshot
- [ ] Enhanced Bubble Chart Screenshot

---

# Key Learning Areas

This project demonstrates:

### Data Engineering

- Data Pipelines
- Workflow Orchestration
- ETL Concepts

### Data Processing

- Web Scraping
- HTML Parsing
- JSON Processing

### Automation

- Airflow
- Docker

### Visualization

- JavaScript
- D3.js
- Bubble Charts

---

# Personal Notes

Project 23.1 is one of the strongest portfolio projects in the MIT Professional Certificate in Data Engineering program because it demonstrates a complete end-to-end pipeline:

```text
Web Data
    ↓
Extraction
    ↓
Cleaning
    ↓
Transformation
    ↓
Analysis
    ↓
JSON
    ↓
Visualization
    ↓
Workflow Automation
```

The project combines web scraping, data engineering, workflow orchestration, and data visualization into a single real-world workflow that resembles modern production analytics systems.