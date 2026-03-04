import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Create a new column called `country_upper` using the string function
# `.str.to_uppercase()` on the column `country`:
result_1 = (gapminder
 .with_columns(country_upper = pl.col("country").str.to_uppercase())
)
print(result_1.select("country", "country_upper").head())

# Create a new column called `gdp_total` which is `pop` multiplied by `gdpPercap`:
result_2 = (gapminder
 .with_columns(gdp_total = pl.col("pop") * pl.col("gdpPercap"))
)
print(result_2.select("country", "year", "gdp_total").head())
