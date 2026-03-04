import polars as pl
from plotnine import *

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Display the evolution of average life expectancy by continent over time
(gapminder
 .group_by(pl.col("_____"), pl.col("_____"))
 .agg(pl.col("_____").mean().alias("m_exp"))
 >>
 ggplot(aes("year", "m_exp", color="_____"))
 + geom_line()
 + labs(y="_____", x="_____")
 + theme_bw()
)
