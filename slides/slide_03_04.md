---
type: slides
---

# Customising Plots

---

# Facets

Faceting splits a visualisation by the values of another variable:

```python
(ggplot(gapminder)
 + aes(x="year", y="lifeExp", color="continent")
 + geom_point()
 + facet_wrap("continent")
 + theme_classic()
)
```

You can specify the number of rows with `nrow` or columns with `ncol`:

```python
facet_wrap("continent", nrow=1)
```

---

# Labels

plotnine has a `labs()` layer to change axis labels and add titles:

```python
(ggplot(gapminder)
 + aes(x="year", y="lifeExp", color="continent")
 + geom_point()
 + facet_wrap("continent", nrow=1)
 + labs(
     x="Year (from 1952 to 2007)",
     y="Life Expectancy",
     title="Evolution of life expectancy per continent"
 )
 + theme_classic()
)
```

---

# Statistics and special effects

`geom_smooth()` displays linear and non-linear trends:

```python
(ggplot(gapminder)
 + aes(x="year", y="lifeExp", color="continent")
 + geom_point()
 + geom_smooth(method="lm")
 + facet_wrap("continent", nrow=1)
 + theme_classic()
)
```

If `method="lm"`, a linear regression is shown. If `method="loess"`, a non-linear regression is shown.

---

# The more we customise, the better...
