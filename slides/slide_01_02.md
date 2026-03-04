---
type: slides
---

# Python Packages

---

# What are packages?

Python packages extend the functionality of Python by providing additional functions, data types, and tools. They are written by a worldwide community of developers and can be installed for free.

A good analogy is that **Python packages are like apps you can download onto a mobile phone**.

---

# Installing and importing packages

The process is very similar to using an app on your phone:

1. **Install the package**: Using `pip install package_name` in your terminal or `!pip install package_name` in Google Colab. You do this once.

2. **Import the package**: Using `import package_name` at the start of your code. You need to do this every time you start a new session.

```python
# Install (only needed once)
# !pip install polars

# Import (needed every session)
import polars as pl
```

---

# Common import patterns

Python has several ways to import packages:

```python
# Import the whole package
import polars

# Import with an alias (most common)
import polars as pl

# Import specific functions
from plotnine import ggplot, aes, geom_point

# Import everything from a package
from plotnine import *
```

The alias pattern (`import polars as pl`) is the most common and is what we will use throughout these tutorials.

---

# Let's import our first package...
