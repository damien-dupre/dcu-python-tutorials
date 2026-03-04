import polars as pl
from plotnine import *

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# 1. Filter for the year 2007
# 2. Group by continent
# 3. Calculate the average life expectancy per continent
# 4. Sort from highest to lowest
# 5. Create a bar chart with continent on x, avg life expectancy on y, filled by continent

(gapminder
 .filter(pl.col("_____") == _____)
 .group_by(pl.col("_____"))
 .agg(pl.col("_____").mean().alias("avg_lifeExp"))
 .sort("avg_lifeExp", descending=True)
 >>
 ggplot(aes(x="_____", y="_____", fill="_____"))
 + geom_col()
 + labs(
     x="Continent",
     y="Average Life Expectancy",
     title="Average Life Expectancy by Continent in 2007"
 )
 + theme_minimal()
)
