import polars as pl

gapminder = pl.read_csv("https://raw.githubusercontent.com/damien-dupre/data/refs/heads/master/gapminder.csv")

# Create two separate tables
table_1 = (gapminder
 .select(pl.col("country"), pl.col("year"), pl.col("pop"))
)
table_2 = (gapminder
 .select(pl.col("country"), pl.col("year"), pl.col("lifeExp"))
)

# Join the two tables on "country" and "year" using an inner join
result = (table_1
 .join(table_2, on=["_____", "_____"], how="_____")
)
print(result.head(10))
