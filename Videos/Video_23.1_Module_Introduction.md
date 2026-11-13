# Module 23: Introduction and Information [Video 23.1]

## Welcome to Module 23: Creating a Data Pipeline

In this module, you will work on another portfolio-worthy project that demonstrates key data engineering and data science concepts. The module introduces **Required Project 23.1: Creating a Sensemaking Data Pipeline**, where you will build an end-to-end pipeline for collecting, processing, analyzing, and visualizing data.

The module also covers several important concepts and technologies related to data visualization and web development, including:

- Structured vs. unstructured data
- JavaScript fundamentals
- JavaScript use cases in web development
- HTML tags
- The Document Object Model (DOM)
- Data visualization using the D3 (Data-Driven Documents) library

As part of the project, you will perform data analysis on unstructured MIT course catalog data and use D3 to create visualizations based on word frequency analysis.

> **Note:** Before beginning this module, ensure you have installed the required tools for Modules 23–24 as outlined in the Course Tools Module.

---

## Project Overview: Creating a Sensemaking Data Pipeline

In this project, you will build a complete sensemaking data pipeline using several technologies introduced throughout the course.

### Project Objectives

You will:

1. Use Python's `urllib` library to retrieve data from MIT's course catalog.
2. Clean and transform the unstructured web data.
3. Extract course titles from the raw content.
4. Analyze the frequency of words appearing across course titles.
5. Save the analysis results as a JSON file.
6. Build a D3-powered web application to visualize the analyzed data.

### Data Pipeline Workflow

```text
MIT Course Catalog
        │
        ▼
Python urllib Extraction
        │
        ▼
Data Cleaning & Transformation
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

### Technologies Used

- Python
- urllib
- JSON
- Docker
- Apache Airflow
- HTML
- JavaScript
- D3.js

### Workflow Orchestration

To streamline processing, the project uses technologies learned in earlier modules:

- **Docker** to containerize the environment
- **Apache Airflow** to orchestrate tasks and workflow execution

You will create multiple Python tasks and manage them through an Airflow web server running inside a Docker container. This approach breaks the project into manageable steps while demonstrating real-world data engineering practices.

### Expected Project Effort

- Estimated completion time: **10 hours**
- Actual time may vary depending on experience level and project customization.

---

## Video 23.1: Introduction (01:14)

### Summary

Deriving meaningful insights from unstructured data can be challenging. In this introductory video, Dr. Sanchez provides an overview of **Required Project 23.1: Creating a Sensemaking Data Pipeline** and explains how students will:

- Extract data from the MIT course catalog
- Transform unstructured content into usable data
- Analyze word frequencies
- Generate data visualizations
- Build a complete sensemaking data pipeline

---

## Key Takeaways

- Unstructured data requires transformation before analysis.
- Data pipelines automate the process of collecting, cleaning, analyzing, and presenting data.
- Python's `urllib` library can be used for web-based data extraction.
- Airflow enables workflow orchestration through task management.
- Docker provides a reproducible runtime environment.
- D3.js is a powerful visualization library for displaying analytical results.
- The project combines data engineering, data analysis, and web development skills into a single portfolio artifact.

---

## Personal Notes

### Why This Module Matters

This project is one of the most comprehensive projects in the program because it integrates:

- Data acquisition
- Data cleaning
- Data transformation
- Workflow orchestration
- Containerization
- Data analysis
- Data visualization

It effectively simulates a real-world data engineering workflow and serves as a strong portfolio example demonstrating an end-to-end data pipeline.

### Concepts to Focus On

- Unstructured vs. Structured Data
- ETL/ELT Concepts
- JSON as an interchange format
- Airflow DAGs
- Docker containers
- JavaScript fundamentals
- DOM manipulation
- D3 visualizations
- Text analytics and word frequency analysis

---

## Transcript

Video transcript available through the course portal.