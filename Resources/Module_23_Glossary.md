# Module 23: Glossary

---

# BeautifulSoup4 Library

**Definition:**  
BeautifulSoup4 is a Python library that enables web scraping and HTML parsing.

**Usage in Module 23:**

- Parse MIT course catalog pages
- Search HTML elements
- Extract course titles from `<h3>` tags
- Transform unstructured HTML into structured data

---

# Data-Driven Documents (D3) Library

**Definition:**  
D3 (Data-Driven Documents) is a JavaScript library used for creating dynamic and interactive data visualizations.

**Applications:**

- Bubble charts
- Bar charts
- Scatter plots
- Dashboards
- Interactive visualizations

**Usage in Module 23:**

- Visualize MIT course title word frequencies
- Build interactive browser-based charts

---

# Document Object Model (DOM)

**Definition:**  
The Document Object Model (DOM) is the structural representation of an HTML document.

The DOM serves as a bridge between:

```text
HTML
    ↕
JavaScript
```

and always follows a tree-like structure.

**Usage in Module 23:**

- Navigate HTML documents
- Locate course title elements
- Extract information from web pages

---

# Domain Name System (DNS) Attack

**Definition:**  
A DNS attack occurs when excessive requests are sent to a network resource, making it unavailable.

**Best Practice:**

Introduce delays between requests:

```python
time.sleep(15)
```

to avoid overwhelming servers.

**Usage in Module 23:**

Used while downloading MIT catalog pages.

---

# Frequency Representation

**Definition:**  
A frequency representation visualizes how often a value appears in a dataset.

**Examples:**

- Word frequency
- Event frequency
- Category frequency

**Usage in Module 23:**

Visualizing how frequently words occur within MIT course titles.

---

# HTML Attribute

**Definition:**  
An HTML attribute provides additional information that configures an HTML element.

**Example:**

```html
<a href="https://mit.edu">
```

Attribute:

```html
href
```

Value:

```html
https://mit.edu
```

---

# HTML Tags

**Definition:**  
HTML tags define and format content on a web page.

**Structure:**

```html
<tag>
    content
</tag>
```

**Examples:**

```html
<html>
<body>
<h1>
<p>
<a>
```

**Usage in Module 23:**

Course titles were extracted from:

```html
<h3>
```

elements.

---

# id Attribute

**Definition:**  
The `id` attribute uniquely identifies an HTML element.

**Example:**

```html
<div id="target"></div>
```

A value assigned to an `id` attribute must be unique within an HTML document.

---

# Interpreter

**Definition:**  
An interpreter reads and executes program code directly without a separate compilation step.

**Examples:**

- Python
- JavaScript

**Benefits:**

- Faster development
- Immediate execution
- Easier debugging

---

# JavaScript

**Definition:**  
JavaScript is a programming language used to create dynamic and interactive content within web browsers.

**Common Uses:**

- Interactive websites
- Data visualizations
- Dashboards
- Browser applications

**Usage in Module 23:**

- D3 visualizations
- Bubble charts
- DOM manipulation

---

# Natural Language Processing (NLP)

**Definition:**  
Natural Language Processing (NLP) is a branch of Machine Learning that focuses on enabling computers to process and understand human language.

**Applications:**

- Sentiment analysis
- Keyword extraction
- Text classification
- Language translation

---

# NLTK Library

**Definition:**  
The Natural Language Toolkit (NLTK) is a popular Python library used for NLP tasks.

**Functions:**

- Tokenization
- Text processing
- Stopword removal
- Text analysis

---

# NotebookJS Library

**Definition:**  
NotebookJS is a library that enables the execution of JavaScript code inside Jupyter notebooks.

**Usage:**

- Educational demonstrations
- Interactive notebook development
- Visualization integration

---

# Polar Coordinates

**Definition:**  
Polar coordinates describe a point using:

1. Distance from the origin
2. Angle from the positive x-axis

**Format:**

```text
(r, θ)
```

Example:

```text
(1, 60°)
```

---

# Radial Bar Chart

**Definition:**  
A radial bar chart uses polar coordinates instead of Cartesian coordinates.

**Characteristics:**

- Circular layout
- Angular categories
- Radial measurements

**Usage in Module 23:**

Created using D3 to visualize word-frequency data.

---

# Stopwords

**Definition:**  
Stopwords are words or symbols that are commonly removed during text analysis because they carry limited analytical value.

**Examples:**

```text
a
an
the
and
```

Punctuation marks are also often treated as stopwords.

---

# Scrape

**Definition:**  
Web scraping is the process of extracting information from web pages automatically.

**Usage in Module 23:**

The MIT course catalog was scraped to collect course titles.

**Process:**

```text
Download HTML
      ↓
Parse HTML
      ↓
Extract Data
```

---

# Switch

**Definition:**  
A JavaScript control-flow statement that evaluates an expression against multiple conditions.

**Example:**

```javascript
switch(value) {

    case 1:
        ...
        break;

    case 2:
        ...
        break;
}
```

---

# Token

**Definition:**  
A token is an individual word extracted from text during tokenization.

**Example:**

Sentence:

```text
Introduction to Data Engineering
```

Tokens:

```text
Introduction
to
Data
Engineering
```

**Usage:**

- Text processing
- NLP
- Word-frequency analysis

---

# Unstructured Data

**Definition:**  
Unstructured data is data that does not follow a predefined schema and cannot be directly stored in traditional relational databases.

**Examples:**

- Emails
- Social media posts
- Images
- Videos
- HTML documents

**Usage in Module 23:**

MIT course catalog HTML pages were treated as unstructured data before being transformed into a structured dataset for analysis.

---

# Key Module 23 Concepts

```text
Unstructured Data
       ↓
HTML
       ↓
DOM
       ↓
BeautifulSoup
       ↓
Course Titles
       ↓
Tokens
       ↓
Word Frequencies
       ↓
JSON
       ↓
D3 Visualization
```

These concepts collectively form the foundation of the **Sensemaking Data Pipeline** implemented in Project 23.1.