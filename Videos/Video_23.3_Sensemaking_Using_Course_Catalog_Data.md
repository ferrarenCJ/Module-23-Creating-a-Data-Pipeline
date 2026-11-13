# Video 23.3: Sensemaking Using Course Catalog Data

**Duration:** 12:24

---

## Overview

In this video, Dr. Sanchez provides a detailed walkthrough of the workflow and technologies that will be used to complete **Project 23.1: Creating a Sensemaking Data Pipeline**.

The project demonstrates how to transform raw, unstructured web data into meaningful insights using a combination of data engineering, data analysis, and visualization techniques.

The video covers:

- Extracting data from the MIT course catalog
- Using curl and Python for data retrieval
- Parsing HTML data using the Document Object Model (DOM)
- Building an automated sensemaking data pipeline
- Creating visualizations using word frequency analysis

---

## Project Objective

The goal of the project is to create a fully automated pipeline that:

1. Collects MIT course catalog data from the web.
2. Extracts useful information from the HTML.
3. Cleans and structures the extracted data.
4. Analyzes course title text.
5. Calculates word frequency statistics.
6. Exports analysis results as JSON.
7. Visualizes findings using a web application powered by D3.

---

# Step 1: Data Extraction

## Retrieving Data from the MIT Course Catalog

The first phase of the project is collecting raw data from MIT's course catalog website.

### Tools Used

#### curl

Command-line tool used to download web content.

Example:

```bash
curl https://catalog.mit.edu/subjects/
```

#### Python

Used to automate retrieval and processing.

Example:

```python
from urllib.request import urlopen

url = "https://catalog.mit.edu/subjects/"
response = urlopen(url)

html = response.read()
```

### Output

```text
Raw HTML
```

At this stage, the data is completely unstructured from an analytical perspective.

---

# Step 2: HTML Parsing

## Working with the DOM

Once the HTML is retrieved, the next task is identifying where useful information resides within the page structure.

### Document Object Model (DOM)

The DOM represents a webpage as a structured tree.

Example:

```html
<html>
    <body>
        <div>
            <a>Course Name</a>
        </div>
    </body>
</html>
```

DOM Structure:

```text
HTML
 └── BODY
      └── DIV
           └── A
```

Using the DOM allows us to:

- Locate course titles
- Ignore unnecessary page content
- Extract specific data elements

---

## Why DOM Parsing Matters

Raw HTML contains:

- Navigation links
- Headers
- Footers
- Styling information
- Metadata

The project focuses on extracting only the portions containing course information.

This transforms:

```text
Unstructured HTML
```

into

```text
Structured Course Data
```

---

# Step 3: Data Transformation

After extracting course names, the data must be cleaned.

### Example

Raw course titles:

```text
Introduction to Computer Science
Data Engineering Fundamentals
Machine Learning
```

The pipeline converts the extracted information into a structured format suitable for analysis.

---

# Step 4: Word Frequency Analysis

The next step is performing text analysis.

### Example

Course Titles:

```text
Introduction to Computer Science
Introduction to Data Engineering
```

Word Counts:

| Word | Frequency |
|--------|-----------|
| Introduction | 2 |
| To | 2 |
| Data | 1 |
| Engineering | 1 |
| Computer | 1 |
| Science | 1 |

The resulting dataset helps identify commonly occurring concepts throughout MIT's course catalog.

---

# Step 5: JSON Generation

The analyzed data is saved as JSON.

### Example

```json
[
  {
    "word": "data",
    "count": 42
  },
  {
    "word": "engineering",
    "count": 18
  }
]
```

### Why JSON?

JSON is:

- Lightweight
- Human-readable
- Easily consumed by JavaScript applications
- Ideal for data exchange between Python and D3

---

# Step 6: Visualization

The final stage of the project is data visualization.

### D3.js

D3 (Data-Driven Documents) is a JavaScript library that creates dynamic visualizations directly in the browser.

### Input

```text
word_frequency.json
```

### Output

Potential visualizations include:

- Bar Charts
- Frequency Charts
- Interactive Visualizations
- Word Frequency Visualizations

The visual output helps users quickly identify the most common themes appearing within MIT's course offerings.

---

# Complete Pipeline Workflow

```text
MIT Course Catalog
        │
        ▼
Data Extraction
(curl / urllib)
        │
        ▼
HTML Content
        │
        ▼
DOM Parsing
        │
        ▼
Course Title Extraction
        │
        ▼
Data Cleaning
        │
        ▼
Word Frequency Analysis
        │
        ▼
JSON Export
        │
        ▼
D3 Visualization
```

---

# Technologies Used

## Data Collection

- curl
- Python urllib

## Data Processing

- HTML
- DOM

## Data Analysis

- Python
- JSON

## Visualization

- JavaScript
- D3.js

## Workflow Automation

- Apache Airflow

## Containerization

- Docker

---

# Key Takeaways

- Web data is often unstructured and requires processing before analysis.
- Python and curl can be used to retrieve content from websites.
- The DOM provides a structured way to navigate HTML documents.
- Extracted data must be transformed into a usable format.
- Word frequency analysis provides a simple but effective sensemaking technique.
- JSON serves as a bridge between Python analysis and D3 visualizations.
- D3 enables interactive and dynamic visual analytics.
- Airflow automates the entire workflow through task orchestration.

---

# Personal Notes

## Pipeline Pattern

This project follows a classic data engineering workflow:

```text
Extract
    ↓
Parse
    ↓
Transform
    ↓
Analyze
    ↓
Store
    ↓
Visualize
```

## Real-World Data Engineering Skills Demonstrated

- Web Scraping
- Data Extraction
- HTML Parsing
- DOM Navigation
- Data Cleaning
- Text Analytics
- JSON Serialization
- Workflow Automation
- Docker Containerization
- Data Visualization

## Portfolio Value

Project 23.1 is one of the strongest portfolio projects in the MIT program because it demonstrates a complete end-to-end data pipeline that combines data engineering, workflow orchestration, analytics, and visualization into a single solution.