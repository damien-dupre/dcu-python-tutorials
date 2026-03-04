import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Summarise the population average by `year` and by `continent`:
result_1 = (gapminder
 .group_by(
     pl.col("year"),
     pl.col("continent")
 )
 .agg(pl.col("pop").mean().alias("pop_average"))
)
print(result_1.sort("year").head(10))

# Summarise the population standard deviation by `year` and by `continent`:
result_2 = (gapminder
 .group_by(
     pl.col("year"),
     pl.col("continent")
 )
 .agg(pl.col("pop").std().alias("pop_std"))
)
print(result_2.sort("year").head(10))
