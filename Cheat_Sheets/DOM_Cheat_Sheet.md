# DOM Cheat Sheet

## DOM Structure

```text
HTML
│
├── HEAD
│
└── BODY
```

---

## Select Element

```javascript
document.getElementById("id")
```

```javascript
document.querySelector(".class")
```

---

## Change Content

```javascript
element.innerHTML = "New Text";
```

---

## Change Style

```javascript
element.style.color = "blue";
```

---

## Event Handling

```javascript
button.onclick = function() {
    alert("Clicked");
}
```

---

## Create Element

```javascript
document.createElement("p")
```

---

## Remove Element

```javascript
element.remove()
```