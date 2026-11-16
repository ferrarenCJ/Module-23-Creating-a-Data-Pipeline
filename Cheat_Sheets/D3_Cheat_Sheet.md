# D3.js Cheat Sheet

## Load D3

```html
<script src="https://d3js.org/d3.v7.min.js"></script>
```

---

## Select Element

```javascript
d3.select("#target")
```

---

## Append Element

```javascript
.append("circle")
```

---

## Bind Data

```javascript
.data(dataset)
```

---

## Create SVG

```javascript
var svg = d3.select("body")
    .append("svg")
    .attr("width", 800)
    .attr("height", 600);
```

---

## Create Circle

```javascript
svg.append("circle")
    .attr("cx", 100)
    .attr("cy", 100)
    .attr("r", 50);
```

---

## Common Visualizations

- Bubble Charts
- Bar Charts
- Scatter Plots
- Line Charts
- Force Graphs
- Treemaps
- Network Diagrams

---

## Tooltips

```javascript
.on("mouseover", tip.show)
.on("mouseout", tip.hide)
```