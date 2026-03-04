---
type: slides
---

# Joining DataFrames

---

# Join two tables

Two different tables sharing a key variable can be merged into one. There are different types of joins:

- **left**: Keep all rows from the left table
- **right**: Keep all rows from the right table
- **inner**: Keep only rows that match in both tables
- **full**: Keep all rows from both tables

---

# Join with same column name

```python
table_1 = (gapminder
 .select(pl.col("country"), pl.col("year"), pl.col("pop"))
)
table_2 = (gapminder
 .select(pl.col("country"), pl.col("year"), pl.col("lifeExp"))
)

(table_1
 .join(table_2, on=["country", "year"], how="inner")
)
```

---

# Join with different column names

When the key columns have different names, use `left_on` and `right_on`:

```python
(table_1
 .join(
     table_2,
     left_on=["country", "year"],
     right_on=["country_measure", "year_measure"]
 )
)
```

---

# Let's practise joining...
