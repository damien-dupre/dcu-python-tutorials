---
type: slides
---

# The with_columns() function

---

# The `with_columns()` function

It is often useful to add new columns that are functions of existing columns. That is the job of `with_columns()`.

For example, we can create a new column called `gdp_total`:

```python
(gapminder
 .with_columns(gdp_total = pl.col("pop") * pl.col("gdpPercap"))
)
```

`with_columns()` can create multiple columns in the same statement, separated by commas.

---

# Useful creation expressions

There are many expressions you can use with `with_columns()`:

- Arithmetic: `pl.col("a") + pl.col("b")`
- String operations: `pl.col("name").str.to_uppercase()`
- Conditional: `pl.when(condition).then(value).otherwise(other)`
- Mathematical functions: `pl.col("x").log()`, `pl.col("x").sqrt()`

---

# Time for creating some new columns...
