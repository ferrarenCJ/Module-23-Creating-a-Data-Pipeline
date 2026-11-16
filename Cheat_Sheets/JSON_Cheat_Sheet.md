# JSON Cheat Sheet

## Object

```json
{
    "name": "MIT",
    "count": 50
}
```

---

## Array

```json
[
    {
        "name": "MIT"
    },
    {
        "name": "Harvard"
    }
]
```

---

## Read JSON

```python
import json

with open("file.json") as f:
    data = json.load(f)
```

---

## Write JSON

```python
with open("file.json", "w") as f:
    json.dump(data, f, indent=4)
```

---

## Common Uses

- API Data
- Configuration Files
- Data Exchange
- D3 Visualization Data

---

## Python Dictionary to JSON

```python
json.dump(data, f)
```

---

## JSON to Python

```python
json.load(f)
```