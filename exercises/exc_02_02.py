import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Display the first 5 rows of the gapminder DataFrame
print(gapminder._____(5))

# Display summary statistics of the gapminder DataFrame
print(gapminder._____())
