# Mini-Lesson 23.4: The Document Object Model (DOM)

---

## Overview

The **Document Object Model (DOM)** is one of the most important concepts in web development and data extraction.

The DOM serves as a bridge between:

- HTML pages
- JavaScript
- User interactions

It allows developers to:

- Read web page content
- Modify web page content
- Analyze HTML structures
- Extract information from websites

For data engineers, understanding the DOM is particularly important because it enables the parsing and extraction of data from web pages during web scraping and data pipeline development.

---

# What Is the DOM?

Imagine using a remote control to interact with a sound system.

The remote control allows you to:

- Change channels
- Adjust volume
- Modify settings

without physically opening or altering the sound system itself.

The DOM operates similarly for web pages.

```text
JavaScript
      │
      ▼
    DOM
      │
      ▼
 HTML Page
```

JavaScript communicates with the DOM, and the DOM updates what users see in the browser.

---

## Example

Suppose a webpage title is displayed in blue.

By modifying JavaScript, you could change the title to red:

```javascript
document.getElementById("title").style.color = "red";
```

The DOM updates the webpage automatically without requiring manual changes to the displayed content.

---

# Why the DOM Is Important

The DOM enables developers to:

## Modify Existing Content

Example:

```javascript
document.getElementById("header").innerHTML =
    "Welcome to MIT Data Engineering";
```

---

## Create New Content

Example:

```javascript
const paragraph =
    document.createElement("p");
```

---

## Remove Content

Example:

```javascript
element.remove();
```

---

## Handle User Interaction

Examples:

- Button clicks
- Form submissions
- Navigation events
- Dynamic updates

---

# DOM as a Data Engineering Tool

The DOM is not only useful for website development.

Data engineers frequently use the DOM when working with:

```text
Unstructured HTML Data
```

The DOM makes it possible to:

- Inspect web pages
- Locate specific content
- Identify HTML tags
- Extract information
- Convert data into structured formats

---

## Example

HTML:

```html
<h3>Introduction to Data Engineering</h3>

<h3>Database Systems</h3>

<h3>Machine Learning</h3>
```

DOM View:

```text
HTML
 └── BODY
      ├── H3
      ├── H3
      └── H3
```

A scraper can navigate the DOM and extract each course title.

---

# How Is the DOM Structured?

The DOM always follows a **tree structure**.

Every element becomes a node.

Example HTML:

```html
<html>

<head>

<title>
Here is information about the data engineering course.
</title>

</head>

<body>

<h1>
Data engineering deals with databases.
</h1>

<p>
The above text is an introduction.
</p>

</body>

</html>
```

---

# DOM Tree Representation

The HTML above becomes:

```text
HTML
├── HEAD
│     └── TITLE
│
└── BODY
      ├── H1
      └── P
```

---

# Parent and Child Nodes

DOM elements maintain hierarchical relationships.

## Parent Node

Contains other elements.

Example:

```html
<html>
```

acts as the parent of:

```html
<head>
<body>
```

---

## Child Node

Exists inside another element.

Example:

```html
<title>
```

is a child of:

```html
<head>
```

---

# Example Relationships

```text
HTML
├── HEAD
│     └── TITLE
│
└── BODY
      ├── H1
      └── P
```

| Node | Parent |
|--------|---------|
| HEAD | HTML |
| BODY | HTML |
| TITLE | HEAD |
| H1 | BODY |
| P | BODY |

---

# DOM Nodes

Every element in an HTML page becomes a node.

Examples:

```html
<html>
```

```html
<head>
```

```html
<body>
```

```html
<h1>
```

```html
<p>
```

All are nodes within the DOM tree.

---

# HTML Attributes

Elements can also contain attributes.

Attributes add extra configuration to HTML elements.

---

## Example

```html
<a href="https://www.mit.edu">
    MIT
</a>
```

### Element

```html
<a>
```

### Attribute

```html
href
```

### Value

```html
https://www.mit.edu
```

The attribute tells the browser where the hyperlink should navigate.

---

# Visualizing HTML and the DOM

HTML:

```html
<body>

<h1>MIT Courses</h1>

<a href="https://www.mit.edu">

MIT Website

</a>

</body>
```

DOM:

```text
BODY
├── H1
└── A
     └── href
```

The DOM organizes page content into a structure that JavaScript can understand and manipulate.

---

# JavaScript and the DOM

JavaScript interacts with elements through the DOM.

Common operations:

### Find Elements

```javascript
document.getElementById()
```

```javascript
document.querySelector()
```

---

### Change Content

```javascript
element.innerHTML = "New Text";
```

---

### Change Styling

```javascript
element.style.color = "blue";
```

---

### Respond to Events

```javascript
button.onclick = function() {
    alert("Clicked");
}
```

---

# Project 23.1 Connections

The DOM plays a critical role in the Sensemaking Data Pipeline project.

---

## Data Sources

You will retrieve:

```text
MIT Course Catalog HTML Pages
```

These files are considered:

```text
Unstructured Data
```

---

## Pipeline Workflow

```text
MIT Course Catalog
        │
        ▼
Download HTML Files
        │
        ▼
Concatenate Files
        │
        ▼
Parse HTML
        │
        ▼
Traverse DOM
        │
        ▼
Locate Course Titles
        │
        ▼
Extract Words
        │
        ▼
Count Frequencies
        │
        ▼
Generate JSON
        │
        ▼
D3 Visualization
```

---

# Identifying Course Titles

The course catalog stores titles within specific HTML tags.

Example:

```html
<h3>
Introduction to Data Engineering
</h3>
```

Using DOM traversal and HTML parsing, the pipeline can identify:

```html
<h3>
```

elements and retrieve the enclosed text.

---

# Real-World Data Engineering Applications

The same techniques used in Project 23.1 are used daily by data engineers.

Examples include:

- Scraping product catalogs
- Collecting news articles
- Extracting research papers
- Monitoring competitor pricing
- Aggregating public datasets
- Collecting social media information

In all of these cases, engineers must:

1. Inspect HTML.
2. Understand the DOM structure.
3. Locate relevant tags.
4. Extract useful information.
5. Convert it into structured data.

---

# Key Takeaways

- The DOM is a structured representation of an HTML document.
- JavaScript communicates with webpages through the DOM.
- The DOM follows a hierarchical tree structure.
- Every HTML element becomes a node in the DOM.
- Parent-child relationships define page organization.
- Attributes provide additional information about elements.
- DOM traversal allows developers to locate and manipulate data.
- Data engineers use DOM structures to extract information from web pages.
- Project 23.1 relies heavily on DOM analysis to identify and retrieve MIT course titles.

---

# Personal Notes

## Data Engineering Perspective

The DOM transforms a webpage from:

```text
Raw HTML
```

into:

```text
Structured Tree
```

which makes it much easier to locate specific information.

---

## Most Important Concept for Project 23.1

The workflow is essentially:

```text
HTML
    ↓
DOM
    ↓
Locate <h3> Tags
    ↓
Extract Course Titles
    ↓
Generate Structured Dataset
    ↓
Perform Word Frequency Analysis
```

Understanding the DOM is the key step that enables the transition from unstructured web content to structured, analyzable data.

---

## Connection to Previous Lessons

### Mini-Lesson 23.1

- Structured vs Unstructured Data

### Mini-Lesson 23.3

- HTML Tags

### Mini-Lesson 23.4

- DOM Navigation and Parsing

Together, these concepts form the foundation for Project 23.1's web scraping and data extraction pipeline.