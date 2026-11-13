# Self-Study Knowledge Check 23.1: Visualization, Unstructured Data, and JavaScript

## Overview

**Module:** 23 - Creating a Data Pipeline  
**Type:** Self-Study Knowledge Check  
**Due Date:** November 19, 2026, 4:29 PM UTC  
**Points:** 0  
**Questions:** 9  
**Time Limit:** None  
**Allowed Attempts:** Unlimited

### Learning Outcome Addressed

- Identify key concepts related to visualization, unstructured data, and JavaScript.

### Objective

This knowledge check evaluates understanding of:

- Structured vs. unstructured data
- HTML tags
- The Document Object Model (DOM)
- JavaScript fundamentals
- Data visualization
- D3.js
- Apache Airflow
- Tools used to manage unstructured data

---

# Results Summary

**Attempt 1**

| Metric | Value |
|----------|----------|
| Completion Time | 3 Minutes |
| Score | 0 / 0 |
| Result | All Questions Answered Correctly |

---

# Question 1

## What is unstructured data?

### Correct Answer

✅ **Unstructured data is data that does not come with a predefined structure and cannot be stored in a traditional database.**

### Explanation

Unstructured data lacks a predefined schema, making it difficult to store directly within relational databases.

Examples include:

- Emails
- Social media posts
- Images
- Videos
- HTML web pages

---

# Question 2

## Which of the following categories does the data coming from emails, texts, social media, and weather imagery fall into?

### Correct Answer

✅ **Unstructured data**

### Explanation

Data originating from:

- Emails
- Text messages
- Social media
- Weather imagery

does not have a predefined schema and therefore qualifies as unstructured data.

---

# Question 3

## What does DOM stand for?

### Correct Answer

✅ **Document Object Model**

### Explanation

The DOM is a tree-structured representation of an HTML document that allows JavaScript to:

- Read content
- Modify content
- Add elements
- Remove elements

---

# Question 4

## What are HTML tags?

### Correct Answer

✅ **HTML tags are used to define and format the way content will appear on a web page.**

### Explanation

HTML tags determine:

- Headings
- Paragraphs
- Links
- Images
- Lists
- Page structure

Example:

```html
<h1>Title</h1>

<p>Paragraph</p>
```

---

# Question 5

## What is the D3 library used for?

### Correct Answer

✅ **D3 is a JavaScript library used for visualization.**

### Explanation

D3 stands for:

**Data-Driven Documents**

D3 is used to:

- Create charts
- Create dashboards
- Generate interactive visualizations
- Bind data directly to DOM elements

---

# Question 6

## Which of the following tools can be used to manage unstructured data?

### Correct Answer

✅ **All of the answer options are correct.**

### Explanation

The lesson identified multiple technologies that help process unstructured data:

- Machine Learning (ML)
- Artificial Intelligence (AI)
- Natural Language Processing (NLP)

These techniques help extract information from large amounts of unstructured content.

---

# Question 7

## What is Airflow used for?

### Correct Answer

✅ **Airflow can be used to create fully automated data engineering pipelines.**

### Explanation

Apache Airflow is a workflow orchestration platform used to:

- Schedule tasks
- Manage dependencies
- Automate pipelines
- Monitor workflow execution

Example:

```text
Extract
    ↓
Transform
    ↓
Analyze
    ↓
Visualize
```

Airflow automates execution from beginning to end.

---

# Question 8

## What are reserved words in JavaScript?

### Correct Answer

✅ **Reserved words are keywords that have specific meaning in a code block and cannot be used to define variables.**

### Explanation

Examples:

```javascript
function
return
for
break
continue
switch
var
```

These keywords are reserved by the JavaScript interpreter and cannot be reused as variable names.

---

# Question 9

## Which D3 function can you call to enhance the appearance of a bubble chart by, for example, adding the frequency of each word to the corresponding bubble?

### Correct Answer

✅ **append()**

### Explanation

The D3 `append()` function is used to add new elements to a visualization.

Examples:

```javascript
node.append("circle")
```

Creates a bubble.

```javascript
node.append("text")
```

Adds labels and frequency counts.

---

# Key Concepts Review

## Unstructured Data

Examples:

- Emails
- Social Media
- Text Messages
- Images
- Videos
- HTML Documents

---

## DOM

Stands for:

```text
Document Object Model
```

Allows JavaScript to interact with web pages.

---

## HTML Tags

Examples:

```html
<h1>
<p>
<a>
<body>
<html>
```

Used to define page structure and formatting.

---

## D3.js

Used for:

```text
Data Visualization
```

Common visualizations:

- Bubble Charts
- Bar Charts
- Scatter Plots
- Line Charts
- Dashboards

---

## JavaScript Reserved Words

Examples:

```javascript
function
return
switch
for
var
continue
break
```

Cannot be used as variable names.

---

## Airflow

Used for:

```text
Workflow Orchestration
```

and

```text
Automated Data Engineering Pipelines
```

---

# Personal Notes

### Most Important Topics for Project 23.1

```text
Unstructured Data
        ↓
HTML
        ↓
DOM
        ↓
Course Title Extraction
        ↓
Word Frequency Analysis
        ↓
JSON Output
        ↓
D3 Visualization
```

### Technologies Used in Module 23

#### Data Collection

- Python
- urllib

#### Data Processing

- HTML
- DOM

#### Automation

- Docker
- Apache Airflow

#### Visualization

- JavaScript
- D3.js

#### Data Exchange

- JSON

The knowledge check serves as a condensed review of every major concept required to complete **Project 23.1: Creating a Sensemaking Data Pipeline**.