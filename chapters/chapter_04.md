---
title: 'Chapter 4: Putting It All Together'
description:
  'This chapter combines everything you have learned to perform complete data analysis workflows, from loading data to creating publication-ready visualisations.'
prev: /chapter_03
next: null
type: chapter
id: 4
---

<exercise id="1" title="Complete workflow" type="slides">

<slides source="slide_04_01">
</slides>

</exercise>

<exercise id="2" title="Questions: Test your knowledge of Polars">

What does the `pl.col()` function do in Polars?

<choice>

<opt text="It creates a new column">

`pl.col()` is used to reference an existing column, not create one. Try again.

</opt>

<opt text="It references an existing column in a DataFrame" correct="true">

Well done! `pl.col("name")` is how you reference columns in Polars expressions.

</opt>

<opt text="It filters the data">

Filtering is done with `.filter()`. Try again.

</opt>

</choice>

Which Polars method is used to create new columns?

<choice>

<opt text="select()">

`select()` keeps or renames existing columns. Try again.

</opt>

<opt text="filter()">

`filter()` subsets rows based on conditions. Try again.

</opt>

<opt text="with_columns()" correct="true">

Well done! `with_columns()` adds or modifies columns in a DataFrame.

</opt>

</choice>

</exercise>

<exercise id="3" title="Questions: Test your knowledge of plotnine">

In plotnine, what does `aes()` stand for?

<choice>

<opt text="Aesthetic mapping" correct="true">

Well done! `aes()` maps variables in your data to visual properties of the plot.

</opt>

<opt text="Axis element settings">

Not quite. `aes()` stands for aesthetic mapping. Try again.

</opt>

<opt text="Automatic export settings">

Not quite. Try again.

</opt>

</choice>

How do you add a linear trend line to a scatter plot in plotnine?

<choice>

<opt text="geom_line(method='lm')">

`geom_line()` draws lines connecting data points. Try again.

</opt>

<opt text="geom_smooth(method='lm')" correct="true">

Well done! `geom_smooth(method='lm')` adds a linear regression trend line.

</opt>

<opt text="geom_trend(type='linear')">

This function does not exist in plotnine. Try again.

</opt>

</choice>

</exercise>

<exercise id="4" title="Exercise: Complete data analysis">

Perform a complete analysis of the gapminder data: load, transform, and visualise:

<codeblock id="04_04">

Replace the `_____` with the correct code.

</codeblock>

</exercise>

<exercise id="5" title="Conclusion">

Congratulations! You've completed all the DCU Python Tutorials.

You now have the skills to wrangle data with Polars and create beautiful visualisations with plotnine. The best way to improve is to practice with your own data and projects.

Here are some resources to continue learning:

- [Polars official user guide](https://docs.pola.rs/)
- [plotnine documentation](https://plotnine.org/)
- [Modern Polars](https://kevinheavey.github.io/modern-polars/) - Polars vs Pandas comparison

</exercise>
