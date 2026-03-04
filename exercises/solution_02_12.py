import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Chain multiple operations: create gdp_total, select columns, group and aggregate
result = (gapminder
 .with_columns(gdp_total = pl.col("pop") * pl.col("gdpPercap"))
 .select(
     pl.col("gdp_total"),
     pl.col("year"),
     pl.col("continent")
 )
 .group_by(pl.col("year"), pl.col("continent"))
 .agg(pl.col("gdp_total").mean().alias("avg_gdp_total"))
)
print(result.sort("year", "continent").head(10))
