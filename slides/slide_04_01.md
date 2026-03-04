---
type: slides
---

# Complete Workflow

---

# The data analysis workflow

A typical data analysis workflow in Python with Polars and plotnine follows these steps:

1. **Import packages**: `import polars as pl` and `from plotnine import *`
2. **Load data**: `pl.read_csv("file.csv")`
3. **Explore**: `.head()`, `.describe()`, `.shape`
4. **Transform**: `.select()`, `.filter()`, `.with_columns()`, `.group_by().agg()`
5. **Visualise**: `ggplot() + aes() + geom_*()`

---

# Example: Complete analysis

```python
import polars as pl
from plotnine import *

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

(gapminder
 .filter(pl.col("year") == 2007)
 .group_by(pl.col("continent"))
 .agg(pl.col("lifeExp").mean().alias("avg_lifeExp"))
 .sort("avg_lifeExp", descending=True)
 >>
 ggplot(aes(x="continent", y="avg_lifeExp", fill="continent"))
 + geom_col()
 + labs(
     x="Continent",
     y="Average Life Expectancy",
     title="Average Life Expectancy by Continent in 2007"
 )
 + theme_minimal()
)
```

---

# Let's test your knowledge...
