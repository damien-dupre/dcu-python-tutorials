---
type: slides
---

# Introduction to Polars

---

# Data Wrangling and Manipulation

`pandas` is a powerful and widely used Python library for data manipulation and analysis. However, `pandas` syntax can be hard to read and write.

`polars` is a modern DataFrame library that is lightning fast and much more user-friendly than `pandas`.

---

# Data Wrangling with Polars

There are five operations that you will use to do the vast majority of data manipulations:

- **Selection**: Subset variables (pick columns by their names) with `select()`
- **Reduction**: Subset observations (pick rows by their values) with `filter()`
- **Extension**: Make new variables (create new columns with functions of existing columns) with `with_columns()`
- **Aggregation**: Summarise data (collapse many values down to a single summary) with `group_by()` and `agg()`
- **Combination**: Merge two or more datasets using a common variable with `join()`

---

# Load Polars

To load the polars package:

```python
import polars as pl
```

In the following code:

- `pl` is the alias to call functions from the package
- `pl.col("variable_name")` will access a specific column

---

# The gapminder dataset

The dataset used in these tutorials is called `gapminder`. Each row corresponds to a country at a specific year. For each row, we have 6 columns:

- **country**: Name of country.
- **year**: Year of the observation (between 1952 and 2007).
- **pop**: Number of people living in the country.
- **continent**: Which of the five continents the country is part of.
- **lifeExp**: Life expectancy in years.
- **gdpPercap**: Gross domestic product (in US dollars).

```python
gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")
```

---

# The Polars syntax

The following code displays the first 5 rows with the `head()` function:

```python
gapminder.head(5)
```

Instead of the classic style, we will use a Polars syntax using `(` as first character and `)` as last character, spreading the code over multiple lines:

```python
(gapminder
 .head(5)
)
```

This way looks longer but it will be very useful to chain different transformations!

---

# What about having a look at this gapminder dataset?
