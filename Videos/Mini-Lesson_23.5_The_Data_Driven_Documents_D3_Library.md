# Mini-Lesson 23.5: The Data-Driven Documents (D3) Library

---

## Overview

Data visualization is an essential component of data engineering and data science. While collecting and processing data are important, visualizing data enables users to quickly identify trends, patterns, and relationships.

One of the most powerful visualization frameworks available today is **D3 (Data-Driven Documents)**.

In this lesson, you will learn:

- What D3 is
- How D3 interacts with the DOM
- How D3 visualizes data
- How to create a bubble chart
- How D3 connects to Project 23.1

---

# What Is D3?

## Definition

**D3 (Data-Driven Documents)** is a JavaScript library designed for creating dynamic and interactive data visualizations within web browsers.

Unlike many charting tools that generate visualizations automatically, D3 provides detailed control over:

- Data binding
- Visual representations
- DOM manipulation
- User interaction
- Animations

The core idea behind D3 is:

> Bind data directly to elements within the DOM and dynamically manipulate those elements based on the data.

---

# How D3 Works

D3 connects three major components:

```text
Data
  ↓
D3 Library
  ↓
DOM Manipulation
  ↓
Visualization
```

D3 takes data and transforms it into:

- Charts
- Graphs
- Dashboards
- Maps
- Network Diagrams
- Bubble Charts

---

# Why D3 Is Powerful

D3 provides substantially more flexibility than traditional charting libraries.

Benefits include:

- Complete control over visualization design
- Direct DOM manipulation
- Interactive graphics
- Animation support
- Dynamic updates
- Browser-based rendering

---

# Examples of D3 Visualizations

Common D3 visualizations include:

### Charts

- Bar Charts
- Pie Charts
- Line Charts
- Area Charts

### Statistical Visualizations

- Histograms
- Scatter Plots
- Box Plots

### Advanced Visualizations

- Tree Maps
- Network Graphs
- Force Diagrams
- Geographic Visualizations

### Text-Based Visualizations

- Word Clouds
- Word Frequency Charts
- Bubble Charts

---

# D3 and Project 23.1

In Project 23.1, D3 will visualize:

```text
Words Extracted from MIT Course Titles
```

and:

```text
Word Frequency Counts
```

Example:

| Word | Count |
|--------|--------|
| Data | 58 |
| Systems | 42 |
| Engineering | 37 |
| Machine | 29 |

These frequencies are displayed as bubbles of varying sizes.

---

# Loading D3

D3 can be included through a Content Delivery Network (CDN).

Example:

```html
<script
src="https://d3js.org/d3.v7.min.js">
</script>
```

This downloads the D3 library directly from the internet without local installation.

---

# Bubble Chart Example

The lesson introduces a bubble chart visualization.

A bubble chart uses circles to represent data values.

### Larger Bubble

```text
Higher Frequency
```

### Smaller Bubble

```text
Lower Frequency
```

---

# Step 1: Create the Dataset

The visualization begins with a dataset.

Example:

```javascript
dataset = {
    "children": [
        {"Name":"Olivia","Count":78},
        {"Name":"Mark","Count":35},
        {"Name":"Jessica","Count":30},
        {"Name":"Alex","Count":55}
    ]
};
```

---

## Dataset Structure

Each item contains:

### Name

```javascript
"Name":"Olivia"
```

The displayed label.

### Count

```javascript
"Count":78
```

The frequency value used to determine bubble size.

---

## Data Representation

```text
Olivia   → 78
Mark     → 35
Jessica  → 30
Alex     → 55
```

---

# Step 2: Create the Bubble Circles

D3 generates a circle for each data item:

```javascript
node.append("circle")
    .attr("r", function(d) {
        return d.r;
    })
    .style("fill", function(d,i) {
        return color(i);
    });
```

---

## What This Code Does

### append("circle")

Creates a circle element.

### attr("r")

Sets the radius.

### style("fill")

Sets bubble color.

---

## Visual Result

```text
Dataset
   ↓
Create Circle
   ↓
Size Based on Count
   ↓
Assign Color
```

---

# Step 3: Add Word Labels

Labels identify each bubble.

Example:

```javascript
node.append("text")
    .attr("dy", ".2em")
    .style("text-anchor", "middle")
    .text(function(d) {
        return d.data.Name;
    });
```

---

## Purpose

Displays:

```text
Olivia
Mark
Jessica
Alex
```

inside their corresponding circles.

---

## Text Scaling

The lesson scales font size according to bubble size.

Example:

```javascript
.attr("font-size", function(d){
    return d.r/5;
})
```

Benefit:

```text
Large Bubble
      ↓
Large Text

Small Bubble
      ↓
Small Text
```

---

# Step 4: Add Frequency Counts

A second label displays the frequency count.

Example:

```javascript
node.append("text")
    .attr("dy", "1.3em")
    .text(function(d) {
        return d.data.Count;
    });
```

---

## Output

Each bubble contains:

```text
Olivia
   78
```

```text
Mark
 35
```

```text
Jessica
 30
```

---

# Final Bubble Chart Structure

Each bubble contains:

```text
Word
Frequency
```

The circle size communicates importance.

Example:

```text
Data      → Large Bubble
Science   → Medium Bubble
Math      → Small Bubble
```

---

# Exploring the Example

After downloading the provided file:

```text
d3_bubble_chart_example.html
```

you can open it in a browser.

Recommended approach:

### Using Live Server

Right-click:

```text
d3_bubble_chart_example.html
```

Select:

```text
Open with Live Server
```

This avoids local browser security restrictions and provides automatic refresh while editing.

---

# D3 and the DOM

One of D3's greatest strengths is its direct interaction with the DOM.

Workflow:

```text
Dataset
      ↓
D3
      ↓
DOM Manipulation
      ↓
SVG Elements
      ↓
Visual Output
```

Every circle, label, color, and animation becomes a DOM element controlled through JavaScript.

---

# Project 23.1 Connections

The bubble chart example serves as the foundation for the module project.

---

## Project Workflow

```text
MIT Course Catalog
            ↓
Download HTML Pages
            ↓
Extract Course Titles
            ↓
Parse Words
            ↓
Calculate Frequencies
            ↓
Generate JSON
            ↓
Read JSON with D3
            ↓
Create Bubble Chart
```

---

## Example

Course Titles:

```text
Introduction to Data Engineering
Data Systems
Data Science
```

Word Counts:

```text
Data = 3
Engineering = 1
Systems = 1
Science = 1
```

Possible Bubble Chart:

```text
Large Bubble  → Data
Small Bubble  → Engineering
Small Bubble  → Systems
Small Bubble  → Science
```

---

# Why Data Engineers Should Learn D3

Data engineers commonly build systems that produce:

- Reports
- Dashboards
- Metrics
- Analytical datasets

Visualizing this information is often the final step in delivering value.

D3 provides the flexibility to build custom visualizations beyond what is available in traditional reporting tools.

---

# D3 vs Traditional Charts

| Feature | Traditional Charts | D3 |
|-----------|-----------|-----------|
| Customization | Limited | Extensive |
| Interactivity | Moderate | Advanced |
| DOM Control | Little | Complete |
| Animation | Basic | Advanced |
| Learning Curve | Lower | Higher |
| Flexibility | Moderate | Extremely High |

---

# Key Takeaways

- D3 stands for **Data-Driven Documents**.
- D3 is a JavaScript library for creating interactive visualizations.
- D3 works by binding data to DOM elements.
- Visualizations are generated dynamically through JavaScript.
- Bubble charts represent values using circle size.
- Labels and frequency counts can be added directly to bubbles.
- D3 visualizations run inside web browsers.
- Project 23.1 uses D3 to visualize word frequencies in MIT course titles.

---

# Personal Notes

## Data Engineering Perspective

Project 23.1 combines multiple technologies into a complete analytics workflow:

```text
HTML Scraping
      ↓
Data Cleaning
      ↓
Word Frequency Analysis
      ↓
JSON Dataset
      ↓
D3 Visualization
```

This mirrors real-world analytical systems where engineers transform raw data into visual insights.

---

## Most Important Concept

D3 is not simply a charting library.

The real power of D3 is:

```text
Data
      ↓
DOM Manipulation
      ↓
Custom Visualization
```

This direct connection between data and the DOM enables virtually unlimited visualization possibilities.

---

## Technologies Introduced in Module 23

### Data Collection

- Python
- urllib

### Data Processing

- HTML
- DOM

### Automation

- Docker
- Apache Airflow

### Visualization

- JavaScript
- D3.js

### Data Exchange

- JSON

Together, these technologies form the complete Sensemaking Data Pipeline architecture used in Project 23.1.