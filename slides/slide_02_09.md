---
type: slides
---

# The group_by() and agg() functions

---

# Summarise your data

You can summarise data with functions like `mean()`, `sum()`, `std()`, `median()`, `len()`:

```python
(gapminder
 .select(pl.col("pop").mean().alias("pop_average"))
)
```

---

# The `group_by()` and `agg()` functions

Summarising is most useful when done for multiple groups with `group_by()` and `agg()`.

For example, the average population per year:

```python
(gapminder
 .group_by(pl.col("year"))
 .agg(pl.col("pop").mean().alias("pop_average"))
)
```

Together `group_by()` and `agg()` provide one of the tools you will use most commonly: grouped summaries.

---

# Let's summarise some data...
