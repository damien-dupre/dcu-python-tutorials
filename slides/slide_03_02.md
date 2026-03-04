---
type: slides
---

# The Grammar of Graphics

---

# The Grammar of Graphics

**"The grammar of graphics"** (the "gg" in ggplot) defines a set of rules for constructing statistical graphics by combining different types of layers.

The mandatory layers from first to last are:

- **Data**: the DataFrame to plot
- **Aesthetics**: the mapping of variables to visual properties (x, y, colour, etc.)
- **Geometries**: the shapes used to represent the data (points, lines, bars, etc.)

Optional layers include themes, facets, labels, and statistics.

---

# Data

The data layer is the name of the object that contains the variables to plot. The visualisation is initiated with `ggplot()`:

```python
(ggplot(data=gapminder)
)
```

Only a grey frame is displayed! We need to define the aesthetics and geometries.

**Layers in plotnine are added with the `+` symbol.**

---

# Aesthetic mapping

The aesthetic mapping refers to the frame of the plot. `x` for the x-axis, `y` for the y-axis, and more. The mapping is done with `aes()`:

```python
(ggplot(data=gapminder)
 + aes(x="gdpPercap", y="lifeExp", color="continent")
)
```

Aesthetic mapping can also include `color`, `fill`, `shape`, `size`, and `group`.

---

# Geometries

Geometries are shapes we use to represent our data. Each starts with `geom_`:

|function          |shape    |
|------------------|---------|
|`geom_point()`    |point    |
|`geom_line()`     |line     |
|`geom_col()`      |bar      |
|`geom_histogram()`|histogram|
|`geom_boxplot()`  |boxplot  |

---

# Putting it together

```python
(ggplot(data=gapminder)
 + aes(x="gdpPercap", y="lifeExp", color="continent")
 + geom_point()
)
```

---

# Themes

To make the plot more professional, add a theme:

```python
(ggplot(gapminder)
 + aes(x="gdpPercap", y="lifeExp", color="continent")
 + geom_point()
 + theme_bw()
)
```

Built-in themes include `theme_bw()`, `theme_classic()`, `theme_minimal()`, `theme_dark()`, `theme_light()`, `theme_void()`, and more.

---

# Time to visualise...
