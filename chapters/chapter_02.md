---
title: 'Chapter 2: Data Wrangling with Polars'
description:
  'This chapter introduces the Polars library for data wrangling in Python, covering select, filter, with_columns, group_by, agg, and method chaining.'
prev: /chapter_01
next: /chapter_03
type: chapter
id: 2
---

<exercise id="1" title="Introduction to Polars" type="slides">

<slides source="slide_02_01">
</slides>

</exercise>

<exercise id="2" title="Exercise: A look at the gapminder DataFrame">

First, we need to import the `polars` package and load the `gapminder` dataset using `pl.read_csv()`. Then, we can look at its structure using `head()` and `describe()`:

<codeblock id="02_02">

Replace the `_____` with the correct function names.

</codeblock>

</exercise>

<exercise id="3" title="The select() function" type="slides">

<slides source="slide_02_03">
</slides>

</exercise>

<exercise id="4" title="Exercise: Practice with select()">

Use the `select()` function to keep and rename specific columns from the gapminder DataFrame:

<codeblock id="02_04">

Replace the `_____` with the column names and aliases.

</codeblock>

</exercise>

<exercise id="5" title="The filter() function" type="slides">

<slides source="slide_02_05">
</slides>

</exercise>

<exercise id="6" title="Exercise: Practice with filter()">

Use the `filter()` function to keep specific observations from the gapminder DataFrame:

<codeblock id="02_06">

Replace the `_____` with the correct values and column names.

</codeblock>

</exercise>

<exercise id="7" title="The with_columns() function" type="slides">

<slides source="slide_02_07">
</slides>

</exercise>

<exercise id="8" title="Exercise: Practice with with_columns()">

Use the `with_columns()` function to create new columns in the gapminder DataFrame:

<codeblock id="02_08">

Replace the `_____` with the correct column names and expressions.

</codeblock>

</exercise>

<exercise id="9" title="The group_by() and agg() functions" type="slides">

<slides source="slide_02_09">
</slides>

</exercise>

<exercise id="10" title="Exercise: Practice with group_by() and agg()">

Use the `group_by()` and `agg()` functions to create statistical summaries from the gapminder DataFrame:

<codeblock id="02_10">

Replace the `_____` with the correct column names and functions.

</codeblock>

</exercise>

<exercise id="11" title="Method chaining" type="slides">

<slides source="slide_02_11">
</slides>

</exercise>

<exercise id="12" title="Exercise: Practice method chaining">

Use method chaining to combine multiple transformations on the gapminder DataFrame:

<codeblock id="02_12">

Replace the `_____` with the correct column names and values.

</codeblock>

</exercise>

<exercise id="13" title="Joining DataFrames" type="slides">

<slides source="slide_02_13">
</slides>

</exercise>

<exercise id="14" title="Exercise: Practice joining DataFrames">

Use the `join()` function to merge two DataFrames:

<codeblock id="02_14">

Replace the `_____` with the correct arguments.

</codeblock>

</exercise>

<exercise id="15" title="Conclusion">

Congratulations! You've completed the "Data Wrangling with Polars" tutorial.

Polars provides a powerful and readable syntax for data manipulation. The method chaining approach makes your code easy to read and understand. For more information, check out the [Polars official user guide](https://docs.pola.rs/).

</exercise>
