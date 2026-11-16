# BeautifulSoup Notes

## Overview

BeautifulSoup4 is a Python library used to parse HTML and XML documents.

In Project 23.1, BeautifulSoup was used to extract course titles from MIT course catalog pages.

---

# Import

```python
from bs4 import BeautifulSoup
```

---

# Parse HTML

```python
soup = BeautifulSoup(html, "html.parser")
```

---

# Find Elements

## Find All Elements

```python
results = soup.find_all('h3')
```

Returns all matching HTML elements.

---

# Extract Text

```python
for item in results:
    titles.append(item.text)
```

Example:

```html
<h3>Introduction to Data Engineering</h3>
```

Returns:

```text
Introduction to Data Engineering
```

---

# Project 23.1 Usage

```python
soup = BeautifulSoup(html, "html.parser")

results = soup.find_all('h3')

titles = []

for item in results:
    titles.append(item.text)
```

Output:

```text
titles.json
```

---

# Benefits

- Easy HTML parsing
- DOM navigation
- Web scraping support
- Search by tag, class, or attribute

---

# Common Tasks

```python
find()
find_all()
get_text()
```

Used extensively for web scraping and data extraction.