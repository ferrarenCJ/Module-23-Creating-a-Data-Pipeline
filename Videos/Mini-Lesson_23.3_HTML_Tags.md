# Mini-Lesson 23.3: HTML Tags

---

## Overview

HTML (HyperText Markup Language) is the foundational language used to structure content on web pages. HTML uses **tags** to define how content is organized and displayed in a browser.

Understanding HTML tags is essential for:

- Web development
- Web scraping
- Data extraction
- Data visualization
- DOM manipulation

In Project 23.1, HTML knowledge will be critical because course information must be extracted from the MIT Course Catalog's HTML pages.

---

# What Are HTML Tags?

HTML tags define the structure and formatting of web content.

Common content types include:

- Titles
- Headings
- Paragraphs
- Images
- Hyperlinks
- Lists
- Code snippets

A typical HTML tag consists of:

```html
<tag>content</tag>
```

### Components

1. Opening Tag

```html
<tag>
```

2. Content

```html
content
```

3. Closing Tag

```html
</tag>
```

The forward slash (`/`) indicates the closing tag.

---

## Example

```html
<p>This is a paragraph.</p>
```

Output:

```text
This is a paragraph.
```

---

# Common HTML Tags

## HTML Document Structure

### `<html>`

Defines the beginning and end of an HTML document.

Example:

```html
<html>
    ...
</html>
```

---

### `<body>`

Contains all visible content displayed in a web browser.

Example:

```html
<body>
    Content goes here
</body>
```

Examples of content inside the body:

- Text
- Images
- Tables
- Links
- Forms
- Charts

---

### `<title>`

Defines the title shown in the browser tab.

Example:

```html
<title>Module 23 Notes</title>
```

---

# Text Formatting Tags

## `<h1>` through `<h6>`

Defines headings.

Hierarchy:

| Tag | Importance |
|------|-----------|
| `<h1>` | Highest |
| `<h2>` | High |
| `<h3>` | Medium |
| `<h4>` | Lower |
| `<h5>` | Low |
| `<h6>` | Lowest |

Example:

```html
<h1>Main Title</h1>
<h2>Section Title</h2>
<h3>Subsection Title</h3>
```

---

## `<p>`

Defines a paragraph.

Example:

```html
<p>This is a paragraph.</p>
```

---

## `<b>`

Displays text in bold.

Example:

```html
<b>Important Text</b>
```

Output:

**Important Text**

---

# Hyperlinks

## `<a>`

Creates a hyperlink.

Example:

```html
<a href="https://mit.edu">
    Visit MIT
</a>
```

Output:

```text
Visit MIT
```

Clicking redirects the user to another page.

---

# Code Display

## `<code>`

Displays programming code.

Example:

```html
<code>
print("Hello World")
</code>
```

Useful for:

- Programming tutorials
- Technical documentation
- Learning resources

---

# Images and Figures

## `<figure>`

Represents self-contained content.

Examples:

- Images
- Charts
- Diagrams
- Illustrations

Example:

```html
<figure>
    <img src="chart.png">
</figure>
```

Often combined with a caption.

---

# HTML Document Example

```html
<!DOCTYPE html>

<html>

<head>
    <title>Example Page</title>
</head>

<body>

<h1>Course Catalog</h1>

<p>Welcome to MIT Courses.</p>

<a href="https://mit.edu">
    MIT Website
</a>

</body>

</html>
```

---

# Why HTML Matters

HTML provides the structure for nearly every web page on the internet.

Without HTML, browsers would not know how to organize content.

HTML enables:

- Navigation
- Content display
- Data presentation
- User interaction
- Information sharing

---

# Applications of HTML

The lesson highlights several important applications.

## 1. Web Development

HTML provides the structure for websites.

Examples:

- Company websites
- Blogs
- Dashboards
- Portals

---

## 2. API Development

Many web-based APIs return or document results through HTML interfaces.

Examples:

- Documentation pages
- Interactive API explorers

---

## 3. Interactive Images and Games

HTML works with:

- JavaScript
- CSS
- Canvas
- WebGL

to create interactive web experiences.

Examples:

- Browser games
- Interactive graphics
- Simulations

---

## 4. Client-Side Storage

HTML applications can interact with browser storage technologies.

Examples:

- Local Storage
- Session Storage

Used to save information within web browsers.

---

## 5. Web Scraping

One of the most important use cases for data engineers.

Data engineers inspect HTML pages and extract:

- Product information
- Customer reviews
- News articles
- Metadata
- Catalog information

---

# HTML and Web Scraping

Web scraping requires understanding HTML structure.

Example HTML:

```html
<h3>Introduction to Data Engineering</h3>

<h3>Machine Learning Fundamentals</h3>

<h3>Database Systems</h3>
```

A scraper can search for:

```html
<h3>
```

and extract the course titles.

---

# Project 23.1 Connections

## MIT Course Catalog Processing

In Project 23.1:

1. Retrieve MIT course catalog web pages.
2. Inspect the HTML structure.
3. Locate course titles.
4. Extract course names.
5. Analyze word frequencies.
6. Visualize results using D3.

---

## Important Observation

The lesson specifically states:

> Course titles are enclosed within HTML `<h3>` tags.

Example:

```html
<h3>
Introduction to Data Engineering
</h3>
```

This means one of the extraction tasks will likely involve locating all:

```html
<h3>
```

elements.

---

## Workflow Example

```text
MIT Course Catalog HTML
            │
            ▼
Locate <h3> Tags
            │
            ▼
Extract Course Titles
            │
            ▼
Split into Words
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

# HTML Tags and the DOM

HTML tags form a document structure known as the:

## Document Object Model (DOM)

Example:

```html
<body>

    <h1>MIT Courses</h1>

    <h3>Data Engineering</h3>

</body>
```

DOM Tree:

```text
BODY
├── H1
└── H3
```

JavaScript can traverse the DOM and retrieve information from these elements.

---

# Key Takeaways

- HTML tags define the structure of web pages.
- Tags contain opening tags, content, and closing tags.
- Important tags include:
  - `<html>`
  - `<body>`
  - `<title>`
  - `<h1>`–`<h6>`
  - `<p>`
  - `<a>`
  - `<code>`
  - `<figure>`
- HTML is foundational for web development and web scraping.
- Understanding HTML tags helps data engineers extract data from websites.
- In Project 23.1, course titles are stored within `<h3>` tags.
- Extracting data from HTML is a common data engineering task.

---

# Personal Notes

## Data Engineering Perspective

This lesson is less about building websites and more about understanding how data is embedded within web pages.

Many real-world pipelines follow this pattern:

```text
Website
    ↓
HTML
    ↓
Tag Identification
    ↓
Data Extraction
    ↓
Data Cleaning
    ↓
Structured Dataset
```

## Project 23.1 Relevance

Most important takeaway:

```text
MIT Course Titles
        ↓
Stored Inside <h3> Tags
        ↓
Extract During Scraping Process
```

Understanding HTML structure is essential because identifying the correct tags determines whether the pipeline extracts useful data or irrelevant page content.