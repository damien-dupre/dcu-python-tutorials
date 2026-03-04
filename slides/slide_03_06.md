---
type: slides
---

# Combining Polars and plotnine

---

# Combining Polars and plotnine

A very powerful way to create figures is to use a ggplot at the end of data transformations. In plotnine, you can pipe a Polars DataFrame to `ggplot()` using the `>>` operator:

```python
# Classic approach:
(ggplot(data=gapminder)
 + aes(x="gdpPercap", y="lifeExp", color="continent")
 + geom_point()
)

# Using the >> pipe:
(gapminder
 >>
 ggplot(aes(x="gdpPercap", y="lifeExp", color="continent"))
 + geom_point()
)
```

---

# filter() to ggplot()

You can easily display only a subset of data:

```python
(gapminder
 .filter(pl.col("country") == "Ireland")
 >>
 ggplot(aes("year", "lifeExp", color="country"))
 + geom_line()
)
```

---

# group_by() and agg() to ggplot()

Summarise variables per group and display the results:

```python
(gapminder
 .group_by(pl.col("year"), pl.col("continent"))
 .agg(pl.col("pop").mean().alias("m_pop"))
 >>
 ggplot(aes("year", "m_pop", color="continent"))
 + geom_line()
)
```

---

# Polars + plotnine = power!
