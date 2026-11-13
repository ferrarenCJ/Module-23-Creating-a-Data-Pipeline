# Mini-Lesson 23.1: Structured vs. Unstructured Data

---

## Overview

In this section of Module 23, you begin exploring three key topics:

- Visualization
- Unstructured Data
- JavaScript

The lesson introduces the differences between structured and unstructured data and explains why understanding both is important for modern data engineering and data science.

You will also learn how these concepts connect directly to **Project 23.1: Creating a Sensemaking Data Pipeline**, where you will transform unstructured MIT course catalog data into a structured format suitable for analysis and visualization.

---

# Structured Data

## Definition

Structured data is data that follows a predefined format or schema.

The structure allows the data to be:

- Stored efficiently
- Queried easily
- Retrieved quickly
- Analyzed systematically

Typically, structured data is stored within a:

- Relational Database Management System (RDBMS)
- Data Warehouse
- Spreadsheet
- CSV file

---

## Characteristics of Structured Data

### Organized into Rows and Columns

Example:

| Course ID | Course Name | Department |
|------------|------------|------------|
| 101 | Data Engineering | EECS |
| 102 | Machine Learning | EECS |

---

### Predefined Schema

A schema defines:

- Data types
- Column names
- Relationships
- Constraints

Example:

```sql
CREATE TABLE Courses (
    CourseID INT,
    CourseName VARCHAR(100),
    Department VARCHAR(50)
);
```

---

### Easily Queried

Structured data can be searched using SQL:

```sql
SELECT *
FROM Courses
WHERE Department = 'EECS';
```

---

## Examples of Structured Data

- Relational databases
- Data warehouses
- ERP systems
- CRM systems
- Transaction records
- Inventory databases
- Customer tables

---

# Unstructured Data

## Definition

Unstructured data does not have a predefined schema or consistent organizational model.

Because there is no fixed structure, the data cannot easily be stored, queried, or analyzed using traditional relational database techniques.

---

## Characteristics of Unstructured Data

### No Fixed Schema

Unlike a relational database table:

```text
Name | Course | Department
```

unstructured data may consist of free-form text, images, videos, or webpage content.

---

### Difficult to Process

Unstructured data typically requires additional steps:

1. Extraction
2. Parsing
3. Cleaning
4. Transformation
5. Analysis

before useful insights can be generated.

---

## Examples of Unstructured Data

### Text-Based Sources

- Emails
- Articles
- Documents
- PDFs
- Chat messages
- Social media posts

### Multimedia Sources

- Images
- Videos
- Audio recordings

### Web Data

- HTML pages
- Website content
- Course catalogs

### Sensor and Specialized Data

- Satellite imagery
- Weather imagery
- Scientific media files

---

# Why Unstructured Data Matters

One of the most important observations in modern analytics is:

> Most newly generated data today is unstructured.

Organizations generate enormous amounts of:

- Emails
- Documents
- Social media content
- Website content
- Images
- Videos

Although difficult to process, these data sources often contain valuable business insights.

Examples include:

- Customer sentiment analysis
- Product reviews
- News analysis
- Search trends
- Research publications
- Educational content

---

# Tools for Working with Unstructured Data

Because unstructured data is difficult to analyze directly, specialized tools have been developed.

## Machine Learning (ML)

Machine learning algorithms can identify patterns and relationships in large unstructured datasets.

Examples:

- Classification
- Clustering
- Recommendation systems

---

## Artificial Intelligence (AI)

AI systems can interpret:

- Text
- Images
- Audio
- Video

to generate insights and predictions.

---

## Natural Language Processing (NLP)

NLP techniques analyze human language.

Examples include:

- Sentiment analysis
- Keyword extraction
- Text classification
- Topic modeling
- Entity recognition

---

## Specialized Libraries

Many libraries exist specifically to process and analyze unstructured information.

Examples:

- BeautifulSoup
- lxml
- NLTK
- spaCy
- D3.js

---

# D3.js and Unstructured Data

## What is D3?

D3 stands for:

**Data-Driven Documents**

D3 is a JavaScript library designed to create dynamic and interactive data visualizations.

---

## How D3 Helps

D3 can:

- Load data
- Transform data
- Display data visually
- Create interactive dashboards
- Visualize patterns and trends

Common visualizations include:

- Bar charts
- Line charts
- Scatter plots
- Treemaps
- Word frequency visualizations

---

## Connection to Project 23.1

In this module's project, D3 will be used to visualize the frequency of words appearing in MIT course titles.

Workflow:

```text
MIT Course Catalog
        │
        ▼
HTML Data
(Unstructured)
        │
        ▼
Data Cleaning
        │
        ▼
Course Title Extraction
        │
        ▼
Word Frequency Analysis
        │
        ▼
JSON Output
        │
        ▼
D3 Visualization
```

---

# Project 23.1 Connections

## Data Source

The MIT course catalog serves as the project's source data.

Initially, this information exists as:

```text
HTML web pages
```

which are considered unstructured from an analytical perspective.

---

## Challenge

The data is not immediately suitable for:

- Analysis
- Reporting
- Visualization

The project therefore requires you to:

1. Extract course titles
2. Clean the data
3. Structure the information
4. Analyze word frequencies
5. Visualize the results

---

## Transformation Process

### Before

```text
Raw HTML
```

### After

```json
[
  {
    "word": "engineering",
    "count": 25
  },
  {
    "word": "data",
    "count": 18
  }
]
```

This structured output can then be consumed by D3.js.

---

# Structured vs. Unstructured Data Comparison

| Feature | Structured Data | Unstructured Data |
|----------|----------|----------|
| Schema | Predefined | No predefined schema |
| Storage | Databases, tables | Files, web pages, media |
| Querying | SQL | Specialized tools |
| Analysis | Straightforward | Requires preprocessing |
| Flexibility | Lower | Higher |
| Examples | Customer records, transactions | Emails, HTML, images, videos |

---

# Key Takeaways

- Structured data follows a predefined schema and is easy to query using SQL.
- Unstructured data lacks a predefined structure and requires additional processing.
- Most modern data generated today is unstructured.
- Specialized tools such as ML, AI, NLP, and D3 help analyze unstructured data.
- Project 23.1 focuses on transforming unstructured MIT course catalog data into a structured format.
- D3.js will be used to visualize the resulting word frequency analysis.

---

# Personal Notes

## Data Engineering Perspective

This project demonstrates one of the most common real-world data engineering workflows:

```text
Unstructured Data
        ↓
Extraction
        ↓
Cleaning
        ↓
Transformation
        ↓
Structured Dataset
        ↓
Analysis
        ↓
Visualization
```

The ability to convert unstructured data into usable formats is a foundational skill for both data engineers and data scientists.

## Important Connection to Module 23

The primary goal of Project 23.1 is not simply visualization.

The real objective is:

> Transforming unstructured MIT course catalog data into structured information that can be analyzed and visualized automatically through a data pipeline.