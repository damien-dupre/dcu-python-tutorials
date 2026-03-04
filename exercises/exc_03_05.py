import polars as pl
from plotnine import *

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Build a ggplot with boxplots faceted by year, with custom labels
(ggplot(gapminder)
 + aes(x="_____", y="_____", color="_____")
 + geom_boxplot()
 + facet_wrap("_____")
 + labs(x="_____", y="_____", title="Life Expectancy by Continent Over Time")
 + theme_classic()
)
