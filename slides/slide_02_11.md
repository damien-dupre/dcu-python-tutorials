---
type: slides
---

# Method Chaining

---

# Method Chaining

Method chaining allows you to write readable, fluent code by combining multiple operations in sequence:

```python
(gapminder
 .with_columns(gdp_total = pl.col("pop") * pl.col("gdpPercap"))
 .select(
     pl.col("gdp_total"),
     pl.col("year").alias("measure_year"),
     pl.col("pop").alias("total_pop")
 )
 .group_by(pl.col("measure_year"))
 .agg(pl.col("gdp_total").mean().alias("gdp_total_average"))
)
```

It is much easier to write `thing.step1().step2().step3()` than `step3(step2(step1(thing)))`.

Polars is designed to be fluent and can be read easily using method chaining.

---

# Now let's chain some transformations together...
