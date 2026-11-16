# Module 23 Cheat Sheets

## Overview

This folder contains quick-reference guides created throughout **Module 23: Creating a Data Pipeline**.

The cheat sheets summarize the key concepts, commands, syntax, libraries, and technologies used in the module and serve as a compact reference for future projects involving data pipelines, web scraping, workflow automation, and data visualization.

---

# Cheat Sheet Directory

| Cheat Sheet | Purpose |
|------------|----------|
| Airflow_Cheat_Sheet.md | DAG creation, operators, tasks, and workflow orchestration |
| D3_Cheat_Sheet.md | D3.js syntax, SVG creation, and data visualization techniques |
| Docker_Cheat_Sheet.md | Docker and Docker Compose commands used throughout the project |
| DOM_Cheat_Sheet.md | JavaScript DOM manipulation and traversal reference |
| HTML_Tags_Cheat_Sheet.md | Common HTML tags used in web development and web scraping |
| JavaScript_Basics.md | Core JavaScript syntax and programming concepts |
| JSON_Cheat_Sheet.md | JSON structure, reading, writing, and parsing examples |

---

# Module 23 Technology Stack

## Data Collection

- Python
- urllib
- Web Scraping

## Data Processing

- BeautifulSoup4
- JSON
- Text Cleaning

## Workflow Orchestration

- Apache Airflow

## Containerization

- Docker
- Docker Compose

## Web Development

- HTML
- JavaScript
- DOM

## Data Visualization

- D3.js
- Bubble Charts
- Force Layouts

---

# How to Use These Cheat Sheets

These references are intended for:

### Quick Syntax Review

Examples:

```python
json.load()
json.dump()

Counter()

BeautifulSoup()
```

---

### Airflow Development

Examples:

```python
PythonOperator()

BashOperator()

with DAG(...)
```

---

### Docker Administration

Examples:

```bash
docker ps

docker compose up -d

docker logs
```

---

### Web Scraping

Examples:

```python
urllib.request.urlopen()

soup.find_all()
```

---

### D3 Visualization

Examples:

```javascript
d3.select()

append("circle")

data()
```

---

# Recommended Review Order

When revisiting Module 23 concepts:

1. Airflow Cheat Sheet
2. Docker Cheat Sheet
3. HTML Tags Cheat Sheet
4. DOM Cheat Sheet
5. JavaScript Basics Cheat Sheet
6. JSON Cheat Sheet
7. D3 Cheat Sheet

This sequence mirrors the workflow used in Project 23.1.

---

# Project 23.1 Connection

The cheat sheets directly support the implementation of:

**Project 23.1: Creating a Sensemaking Data Pipeline**

Workflow:

```text
MIT Course Catalog
        ↓
urllib
        ↓
BeautifulSoup
        ↓
JSON
        ↓
Airflow
        ↓
Docker
        ↓
JavaScript
        ↓
D3 Visualization
```

---

# Personal Notes

Module 23 introduced one of the most complete end-to-end projects in the MIT Professional Certificate in Data Engineering program.

These cheat sheets were created to provide quick access to commonly used commands, patterns, and syntax encountered while building:

- Airflow DAGs
- Docker environments
- Web scraping workflows
- Word-frequency analysis pipelines
- D3 visualizations

They can be reused in future modules and real-world data engineering projects involving unstructured data processing and workflow automation.