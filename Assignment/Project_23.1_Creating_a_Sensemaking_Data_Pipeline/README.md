# Project 23.1: Creating a Sensemaking Data Pipeline

## MIT Professional Certificate in Data Engineering
### Module 23 - Creating a Data Pipeline

---

# Project Overview

This project focused on designing and implementing a complete **Sensemaking Data Pipeline** capable of extracting, processing, analyzing, and visualizing unstructured data from the MIT Course Catalog.

The project combined multiple technologies introduced throughout the MIT Professional Certificate in Data Engineering program, including:

- Python
- Apache Airflow
- Docker
- BeautifulSoup4
- JSON
- HTML
- JavaScript
- D3.js

The primary goal was to automate the collection of course catalog data, transform the data into a structured format, perform word frequency analysis, and generate interactive visualizations.

---

# Project Objectives

The project was designed to:

1. Extract unstructured HTML data from the MIT Course Catalog.
2. Automate extraction using Python and Airflow.
3. Combine multiple catalog pages into a single source.
4. Parse HTML content using BeautifulSoup4.
5. Extract MIT course titles.
6. Clean extracted data by removing punctuation and unwanted values.
7. Perform word frequency analysis.
8. Export results as JSON.
9. Visualize the analyzed data using D3.js.
10. Orchestrate the entire workflow using Apache Airflow running in Docker.

---

# Technologies Used

## Programming Languages

- Python
- JavaScript
- HTML

## Data Processing

- urllib
- BeautifulSoup4
- JSON
- collections.Counter

## Data Engineering

- Apache Airflow
- Docker
- Docker Compose

## Visualization

- D3.js
- SVG
- JavaScript Force Layouts

---

# Project Architecture

```text
MIT Course Catalog
          │
          ▼
     catalog()
          │
          ▼
 Download HTML Files
          │
          ▼
     combine()
          │
          ▼
      combo.txt
          │
          ▼
      titles()
          │
          ▼
    titles.json
          │
          ▼
       clean()
          │
          ▼
 titles_clean.json
          │
          ▼
   count_words()
          │
          ▼
      words.json
          │
          ▼
       words.js
          │
          ▼
   D3 Visualization
```

---

# Airflow Workflow

The Airflow DAG contained six tasks:

| Task ID | Function |
|----------|----------|
| task_zero | Install BeautifulSoup4 |
| task_one | catalog() |
| task_two | combine() |
| task_three | titles() |
| task_four | clean() |
| task_five | count_words() |

Workflow:

```text
task_zero
      │
      ▼
task_one
      │
      ▼
task_two
      │
      ▼
task_three
      │
      ▼
task_four
      │
      ▼
task_five
```

---

# Python Functions

## catalog()

Purpose:

- Read MIT catalog URLs.
- Download each HTML page.
- Store pages locally.

Features:

- urllib.request
- Exception handling
- Automatic file generation

Output:

```text
m1a.html
m1b.html
...
m22c.html
```

---

## combine()

Purpose:

Combine all catalog HTML files into a single file.

Output:

```text
combo.txt
```

---

## titles()

Purpose:

Extract course titles from HTML using BeautifulSoup4.

Method:

```python
soup.find_all('h3')
```

Output:

```text
titles.json
```

---

## clean()

Purpose:

Prepare title data for analysis.

Processing:

- Remove punctuation
- Remove numeric characters
- Remove one-character words

Output:

```text
titles_clean.json
```

---

## count_words()

Purpose:

Calculate word frequencies.

Method:

```python
Counter(words)
```

Output:

```text
words.json
```

---

# Data Processing Results

The pipeline successfully extracted and analyzed thousands of words from MIT course titles.

Examples of high-frequency words:

| Word | Frequency |
|--------|--------|
| and | 1279 |
| in | 831 |
| of | 450 |
| Engineering | 377 |
| Special | 331 |
| Subject | 246 |
| Design | 234 |
| Seminar | 231 |
| for | 221 |
| Systems | 191 |
| Introduction | 190 |
| Science | 171 |

These frequencies were stored in:

```text
words.json
```

and later converted into:

```text
words.js
```

for visualization.

---

# Visualization Development

## Initial Visualization

The provided:

```text
mitcourses_graph.html
```

file was used to display the generated word-frequency data.

The graph utilized:

- JavaScript
- D3.js
- Force-directed bubble layouts

The visualization displayed:

- Word-frequency relationships
- Relative importance through bubble size
- Interactive tooltips

---

## Enhanced Visualization

The visualization was enhanced to:

### Improvements

- Display the top 100 words
- Show word labels directly on bubbles
- Display frequency counts
- Freeze the force layout after stabilization
- Improve readability
- Create a cleaner presentation

Examples displayed on the final visualization:

```text
and (1279)
in (831)
of (450)
Engineering (377)
Special (331)
Design (234)
Seminar (231)
Systems (191)
Introduction (190)
Science (171)
```

The result was a significantly more informative and user-friendly visualization.

---

# Docker Implementation

Apache Airflow was deployed using Docker.

Services included:

- airflow-webserver
- airflow-scheduler
- airflow-worker
- postgres
- redis
- flower

Benefits:

- Reproducibility
- Isolation
- Simplified deployment
- Consistent execution environment

---

# Challenges Encountered

## File Location Issues

The initial implementation failed because Airflow executed tasks from:

```text
/opt/airflow
```

rather than:

```text
/opt/airflow/dags
```

This caused:

```text
FileNotFoundError: 00_urls.txt
```

Solution:

```python
url_file = os.path.join(
    os.path.dirname(__file__),
    "00_urls.txt"
)
```

---

## Missing Catalog Pages

Several URLs from the catalog list returned:

```text
HTTP Error 404: Not Found
```

Solution:

```python
try:
    ...
except Exception as e:
    ...
```

This allowed the pipeline to continue processing valid catalog pages.

---

# Key Learning Outcomes

This project demonstrated:

## Data Engineering

- ETL Principles
- Workflow Automation
- Airflow DAG Development
- Docker Deployment

## Data Processing

- Web Scraping
- HTML Parsing
- JSON Serialization
- Text Cleaning

## Analytics

- Word Frequency Analysis
- Data Transformation
- Data Aggregation

## Visualization

- D3.js Development
- Force Layouts
- Interactive Graphs
- Bubble Charts

---

# Conclusion

Project 23.1 successfully implemented a complete Sensemaking Data Pipeline capable of collecting unstructured MIT course catalog information and transforming it into meaningful visual insights.

The final solution integrated:

- Python
- Apache Airflow
- Docker
- BeautifulSoup4
- JSON
- JavaScript
- D3.js

into a fully automated workflow.

This project represents a real-world example of how data engineers extract, clean, transform, analyze, and visualize unstructured information using modern data engineering tools and techniques.

---

# Deliverables Completed

✅ Project Structure  
✅ Airflow DAG Development  
✅ Docker Deployment  
✅ MIT Catalog Extraction  
✅ HTML Processing  
✅ Course Title Extraction  
✅ Data Cleaning  
✅ Word Frequency Analysis  
✅ words.json Generation  
✅ words.js Generation  
✅ Original D3 Visualization  
✅ Enhanced D3 Bubble Chart Visualization  
✅ Successful End-to-End Pipeline Execution

## Project Status

**Completed Successfully**