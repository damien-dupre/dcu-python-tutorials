import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Filter the countries with population higher than 1,000,000,000 in 2007:
result_1 = (gapminder
 .filter(
     pl.col("_____") == _____,
     pl.col("_____") > _____
 )
)
print(result_1)

# Filter the countries in Europe with life expectancy lower than 60:
result_2 = (gapminder
 .filter(
     pl.col("_____") == "_____",
     pl.col("_____") < _____
 )
)
print(result_2)
