# D3.js Notes

## Overview

D3 (Data-Driven Documents) is a JavaScript library used to create interactive data visualizations.

In Module 23, D3 was used to create visualizations from MIT course catalog word-frequency data.

---

# Load D3

```html
<script src="https://d3js.org/d3.v7.min.js"></script>
```

---

# Purpose

D3 binds data directly to DOM elements.

Workflow:

```text
Data
   ↓
D3
   ↓
DOM
   ↓
Visualization
```

---

# Common D3 Components

## Select Element

```javascript
d3.select()
```

---

## Bind Data

```javascript
.data()
```

---

## Create Elements

```javascript
.append()
```

Examples:

```javascript
.append("circle")
.append("text")
.append("svg")
```

---

# Bubble Charts

A bubble chart visualizes frequency using circle size.

Example:

```text
Large Bubble
      ↓
High Frequency

Small Bubble
      ↓
Low Frequency
```

---

# Tooltips

```javascript
.on('mouseover', tip.show)
.on('mouseout', tip.hide)
```

---

# Module 23 Visualization Workflow

```text
words.json
      ↓
words.js
      ↓
mitcourses_graph.js
      ↓
D3 Rendering
      ↓
Bubble Chart
```

---

# Enhanced Visualization

Enhancements included:

- Displaying Top 100 words
- Showing labels directly on bubbles
- Displaying frequency counts
- Freezing force layout after stabilization

---

# Key Takeaway

D3 provides complete control over:

- Visual appearance
- Interactivity
- Data presentation

making it one of the most powerful visualization libraries available.