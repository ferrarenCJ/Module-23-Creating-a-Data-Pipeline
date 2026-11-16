# Project 23.1 Checklist

## Project Status

**Assignment:** Required Project 23.1 - Creating a Sensemaking Data Pipeline  
**Module:** Module 23 - Creating a Data Pipeline  
**Status:** ✅ Completed

---

# Part 1: Code Development

## Step 1 – Project Structure

- [x] Created `project-23` folder
- [x] Created `airflow-docker` folder
- [x] Added `code_visualization` folder
- [x] Created `assignment.py`
- [x] Captured screenshot

**Screenshot:** Figure 1

---

## Step 2 – Required Imports

- [x] Imported DAG
- [x] Imported timedelta
- [x] Imported BashOperator
- [x] Imported PythonOperator
- [x] Imported days_ago
- [x] Imported urllib
- [x] Imported time
- [x] Imported glob
- [x] Imported os
- [x] Imported json
- [x] Captured screenshot

**Screenshot:** Figure 2

---

## Step 3 – Helper Functions

- [x] Implemented `pull(url)`
- [x] Implemented `store(data, file)`
- [x] Embedded helpers within `catalog()`
- [x] Captured screenshot

**Screenshot:** Figure 3

---

## Step 4 – catalog()

- [x] Loaded URLs from `00_urls.txt`
- [x] Downloaded MIT catalog pages
- [x] Stored HTML files
- [x] Added delay between requests
- [x] Implemented error handling
- [x] Captured screenshot

**Screenshot:** Figure 4

---

## Step 5 – combine()

- [x] Combined HTML files
- [x] Generated `combo.txt`
- [x] Captured screenshot

**Screenshot:** Figure 5

---

## Step 6 – titles()

- [x] Imported BeautifulSoup4
- [x] Parsed HTML
- [x] Located `<h3>` tags
- [x] Extracted course titles
- [x] Generated `titles.json`
- [x] Captured screenshot

**Screenshot:** Figure 6

---

## Step 7 – clean()

- [x] Removed punctuation
- [x] Removed numeric values
- [x] Removed one-character words
- [x] Generated `titles_clean.json`
- [x] Captured screenshot

**Screenshot:** Figure 7

---

## Step 8 – count_words()

- [x] Imported Counter
- [x] Extracted words
- [x] Counted frequencies
- [x] Generated `words.json`
- [x] Captured screenshot

**Screenshot:** Figure 8

---

## Step 9 – DAG Definition

- [x] Defined DAG
- [x] Defined task_zero
- [x] Defined task_one
- [x] Defined task_two
- [x] Defined task_three
- [x] Defined task_four
- [x] Defined task_five
- [x] Defined task dependencies
- [x] Captured screenshot

**Screenshot:** Figure 9

---

# Part 2: Code Execution

## Step 10 – Docker / Airflow Initialization

- [x] Installed Airflow environment
- [x] Started Docker containers
- [x] Verified scheduler running
- [x] Verified worker running
- [x] Verified webserver running
- [x] Verified Redis running
- [x] Verified PostgreSQL running
- [x] Captured screenshot

**Screenshot:** Figure 10

---

## Step 11 – DAG Execution

- [x] Executed DAG
- [x] Validated task_zero
- [x] Validated task_one
- [x] Validated task_two
- [x] Validated task_three
- [x] Validated task_four
- [x] Validated task_five
- [x] All tasks completed successfully
- [x] Captured screenshot

**Screenshot:** Figure 11

---

## Step 12 – words.js

- [x] Generated `words.json`
- [x] Copied results from Airflow worker
- [x] Created `words.js`
- [x] Verified MIT course frequency data
- [x] Captured screenshot

**Screenshot:** Figure 12

---

## Step 13 – Original Visualization

- [x] Opened `mitcourses_graph.html`
- [x] Loaded generated frequency dataset
- [x] Rendered D3 visualization
- [x] Captured screenshot

**Screenshot:** Figure 13

---

## Step 14 – Enhanced Visualization

- [x] Modified D3 visualization
- [x] Added word labels
- [x] Added frequency counts
- [x] Limited display to Top 100 words
- [x] Improved readability
- [x] Stopped force-layout movement
- [x] Captured screenshot

**Screenshot:** Figure 14

---

# Generated Artifacts

## Raw Data

- [x] Downloaded MIT catalog pages

Examples:

```text
m1a.html
m1b.html
...
m22c.html
```

---

## Processed Files

- [x] combo.txt
- [x] titles.json
- [x] titles_clean.json
- [x] words.json
- [x] words.js

---

## Visualizations

- [x] Original D3 Visualization
- [x] Enhanced Bubble Chart

---

# Submission Package

## Included

- [x] All required screenshots
- [x] Submission Word document
- [x] Project code
- [x] Airflow DAG
- [x] Visualization files

---

# Lessons Learned

- [x] Apache Airflow DAG development
- [x] Docker deployment
- [x] Web scraping
- [x] BeautifulSoup HTML parsing
- [x] JSON data processing
- [x] Word-frequency analysis
- [x] D3 visualization development
- [x] Workflow orchestration

---

# Final Project Status

## ✅ Project Complete

All required project deliverables have been successfully implemented, executed, documented, and submitted.