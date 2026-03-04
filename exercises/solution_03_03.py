import polars as pl
from plotnine import *

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Build a ggplot with a boxplot: x as `continent`, y as `lifeExp`, color as `continent`
(ggplot(gapminder)
 + aes(x="continent", y="lifeExp", color="continent")
 + geom_boxplot()
 + theme_minimal()
)
