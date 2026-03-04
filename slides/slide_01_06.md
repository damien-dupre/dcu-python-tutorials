---
type: slides
---

# Lists and Data Structures

---

# Introducing lists

A list is an ordered collection of items. You create a list using square brackets `[]`:

```python
my_list = [4, 5, 6]
print(my_list)
```

```out
[4, 5, 6]
```

---

# Indexing lists

You can access individual elements using square brackets. **Python indexing starts at 0**, not 1:

```python
my_list = [4, 5, 6]
my_list[0]  # first element
```

```out
4
```

```python
my_list[1]  # second element
```

```out
5
```

---

# Slicing lists

You can access a range of elements using slicing with a colon:

```python
my_list = [4, 5, 6, 7, 8]
my_list[1:3]  # elements at index 1 and 2
```

```out
[5, 6]
```

---

# Lists can contain different types

Lists can contain numbers, strings, booleans, or even other lists:

```python
mixed_list = [42, "hello", True, 3.14]

provinces = ["Connacht", "Leinster", "Munster", "Ulster"]
provinces[1]
```

```out
"Leinster"
```

---

# Useful list operations

```python
provinces = ["Connacht", "Leinster", "Munster", "Ulster"]

len(provinces)  # number of elements
```

```out
4
```

```python
provinces.append("New Province")  # add an element
print(provinces)
```

```out
['Connacht', 'Leinster', 'Munster', 'Ulster', 'New Province']
```

---

# Dictionaries

Dictionaries store key-value pairs using curly braces `{}`:

```python
student = {
    "name": "Alice",
    "age": 21,
    "course": "Business Analytics"
}
student["name"]
```

```out
"Alice"
```

Dictionaries are very useful for structured data and are the basis for DataFrames.

---

# Now, time to practise...
