import polars as pl
from plotnine import *

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Display the evolution of average life expectancy by continent over time
(gapminder
 .group_by(pl.col("year"), pl.col("continent"))
 .agg(pl.col("lifeExp").mean().alias("m_exp"))
 >>
 ggplot(aes("year", "m_exp", color="continent"))
 + geom_line()
 + labs(y="Average Life Expectancy (years)", x="Year")
 + theme_bw()
)
