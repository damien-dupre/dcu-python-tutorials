---
type: slides
---

# Introduction

---

# Introduction

Visualising data is one of the most important tasks facing the data analyst. It is important for two reasons:

Firstly, there is the matter of drawing **presentation graphics**: displaying your data in a clean, visually appealing fashion makes it easier for your reader to understand what you are trying to tell them.

Equally important is drawing **exploratory graphics** that help you learn about the data as you go about analysing it.

---

# Introduction

We will use the **plotnine** package, as it provides an easy way to customise your plots. plotnine is based on the grammar of graphics, the same theory behind R's famous ggplot2 package.

To use plotnine:

```python
from plotnine import *
```

---

# The gapminder dataset

Each row in this table corresponds to a country at a specific year. For each row, we have 6 columns:

- **country**: Name of country.
- **year**: Year of the observation (between 1952 and 2007).
- **pop**: Number of people living in the country.
- **continent**: Which of the five continents the country is part of.
- **lifeExp**: Life expectancy in years.
- **gdpPercap**: Gross domestic product (in US dollars).

---

# Let's have a look at plotnine's layers
