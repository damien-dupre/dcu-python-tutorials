---
type: slides
---

# The filter() function

---

# The `filter()` function

You will want to isolate bits of your data. `filter()` allows you to subset observations based on their values.

For example, filtering the dataset for Ireland only:

```python
(gapminder
 .filter(pl.col("country") == "Ireland")
)
```

---

# Comparisons

To filter effectively, you need comparison operators: `>`, `>=`, `<`, `<=`, `!=` (not equal), and `==` (exactly equal).

The easiest mistake to make is to use `=` instead of `==` when testing for equality. Remember: `=` is for assignment, `==` is for comparison.

---

# Multiple filters and multiple values

Multiple values can be filtered using `is_in()` or `is_between()`. Multiple conditions are separated with commas:

```python
(gapminder
 .filter(
     pl.col("country").is_in(["Germany", "United States"]),
     pl.col("year").is_between(2000, 2007)
 )
)
```

---

# Let's apply some filters...
