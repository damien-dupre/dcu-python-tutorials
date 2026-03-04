import polars as pl
from plotnine import *

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Build a ggplot with boxplots faceted by year, with custom labels
(ggplot(gapminder)
 + aes(x="continent", y="lifeExp", color="continent")
 + geom_boxplot()
 + facet_wrap("year")
 + labs(x="Continent", y="Life Expectancy", title="Life Expectancy by Continent Over Time")
 + theme_classic()
)
