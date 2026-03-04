import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Chain multiple operations: create gdp_total, select columns, group and aggregate
result = (gapminder
 .with_columns(_____ = pl.col("pop") * pl.col("gdpPercap"))
 .select(
     pl.col("_____"),
     pl.col("year"),
     pl.col("continent")
 )
 .group_by(pl.col("_____"), pl.col("_____"))
 .agg(pl.col("_____").mean().alias("avg_gdp_total"))
)
print(result.sort("year", "continent").head(10))
