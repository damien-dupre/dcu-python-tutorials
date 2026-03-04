import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Select the columns `lifeExp` and `gdpPercap` and rename them as
# `life_expectancy` and `gdp_per_capita`:
result = (gapminder
 .select(
     pl.col("_____").alias("life_expectancy"),
     pl.col("_____").alias("_____")
 )
)
print(result.head())
