---
type: slides
---

# The select() function

---

# The `select()` function

It is not uncommon to get datasets with hundreds of variables. `select()` allows you to rapidly zoom in on a useful subset using column names.

```python
(gapminder
 .select(
     pl.col("country"),
     pl.col("year"),
     pl.col("pop")
 )
)
```

Importantly, column names must be explicitly referenced in Polars using the function `pl.col()`.

---

# Select and rename variables

While selecting variables, they can also be renamed using the `alias()` function:

```python
(gapminder
 .select(
     pl.col("country"),
     pl.col("year").alias("measure_year"),
     pl.col("pop").alias("total_pop")
 )
)
```

---

# Let's select some columns...
