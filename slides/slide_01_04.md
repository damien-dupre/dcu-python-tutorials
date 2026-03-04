---
type: slides
---

# Coding Basics

---

# Arithmetic operations

You can use Python as a calculator:

|Operator |Description    |
|:-------:|:-------------:|
|+        |addition       |
|-        |subtraction    |
|*        |multiplication |
|/        |division       |
|**       |exponentiation |
|//       |floor division |
|%        |modulo         |

---

# Arithmetic operations

```python
1 / 200 * 30

(59 + 73 + 2) / 3

2 ** 10
```

```out
0.15

44.666666666666664

1024
```

Python returns the answer to whatever you type in, as long as it can figure it out.

---

# Logical operations

Logical values in Python are `True` and `False` (capitalised). To test conditions, we use comparison operators:

|Operator |Description                   |
|:-------:|:----------------------------:|
|> and <  |greater/less than             |
|>= and <=|greater/less than or equal to |
|==       |exactly equal to              |
|!=       |not equal to                  |

---

# Logical operations

```python
1 < 3

2 >= 4

3 == 3

4 != 4
```

```out
True

False

True

False
```

---

# Variables

A variable stores a value that you can reuse later. In Python, we create variables using the `=` sign:

```python
x = 4
print(x)
```

```out
4
```

The variable now stands for the value it contains:

```python
x = 4
x + 3
```

```out
7
```

---

# Variable naming

Variable names must start with a letter or underscore, and can only contain letters, numbers, and underscores. Python convention is to use **snake_case**:

```python
my_age = 25
first_name = "Damien"
this_is_a_really_long_name = 2.5
```

Python is **case-sensitive**: `my_var` and `My_Var` are different variables!

---

# Calling functions

Python has many built-in functions:

```python
function_name(arg1, arg2, ...)
```

For example, the `range()` function creates a sequence of numbers:

```python
list(range(1, 11))
```

```out
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

The `len()` function returns the length of an object:

```python
len("Hello World")
```

```out
11
```

---

# Let's practise with variables and functions...
