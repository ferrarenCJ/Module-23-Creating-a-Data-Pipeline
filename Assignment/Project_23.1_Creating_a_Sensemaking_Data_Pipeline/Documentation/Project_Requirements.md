# Project 23.1: Creating a Sensemaking Data Pipeline

## Project Information

| Item | Details |
|----------|----------|
| Module | Module 23 - Creating a Data Pipeline |
| Assignment | Required Project 23.1 |
| Points | 100 |
| Submission Type | Word Document |
| Estimated Time | 10 Hours |

---

# Learning Outcomes

- Implement JavaScript tools to visualize word frequency data.
- Create a sensemaking data pipeline.

---

# Project Objective

Develop an automated data pipeline that:

1. Extracts unstructured data from the MIT Course Catalog.
2. Converts the data into a structured format.
3. Performs word-frequency analysis.
4. Stores data as JSON.
5. Visualizes results using D3.js.
6. Executes through Apache Airflow running in Docker.

---

# Technology Stack

## Data Collection

- Python
- urllib

## Data Processing

- BeautifulSoup4
- JSON
- collections.Counter

## Workflow Automation

- Apache Airflow

## Containerization

- Docker
- Docker Compose

## Visualization

- JavaScript
- D3.js

---

# Pipeline Workflow

```text
MIT Course Catalog
        ↓
catalog()
        ↓
Downloaded HTML Files
        ↓
combine()
        ↓
combo.txt
        ↓
titles()
        ↓
titles.json
        ↓
clean()
        ↓
titles_clean.json
        ↓
count_words()
        ↓
words.json
        ↓
words.js
        ↓
D3 Visualization
```

---

# Airflow DAG Structure

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

| Task | Function |
|----------|----------|
| task_zero | Install BeautifulSoup4 |
| task_one | catalog() |
| task_two | combine() |
| task_three | titles() |
| task_four | clean() |
| task_five | count_words() |

---

# Deliverables

## Part 1 – Code Development

1. Project Structure
2. Imports
3. Helper Functions
4. catalog()
5. combine()
6. titles()
7. clean()
8. count_words()
9. DAG Definition

## Part 2 – Code Execution

10. Docker/Airflow Running
11. Successful Airflow DAG Execution
12. words.js
13. Original D3 Visualization
14. Enhanced D3 Visualization

---

# Final Outputs

Generated Files:

```text
combo.txt
titles.json
titles_clean.json
words.json
words.js
```

Visualizations:

```text
mitcourses_graph.html
Enhanced Bubble Chart
```

---

# Project Status

✅ Completed