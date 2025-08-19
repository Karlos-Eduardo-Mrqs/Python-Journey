# 🌀 Bonus — List Comprehensions in Python

## 📌 What is a comprehension?

A **comprehension** is a concise way to create new sequences (like lists, sets, or dictionaries) by applying an expression to each item in an iterable.

They help make your code **cleaner, shorter, and often more readable**.

```python
# Traditional way
squares = []
for i in range(5):
    squares.append(i * i)

# With list comprehension
squares = [i * i for i in range(5)]
```

---

## 🧩 List Comprehension — Syntax

```python
[expression for item in iterable if condition]
```

* `expression`: what you want to do with each item
* `item`: each element from the iterable
* `condition` (optional): filter which items to include

### ✅ Examples

```python
# All even numbers from 0 to 10
evens = [x for x in range(11) if x % 2 == 0]

# Square of numbers from 1 to 5
squares = [x**2 for x in range(1, 6)]

# Convert list of strings to uppercase
words = ["python", "rocks"]
upper = [word.upper() for word in words]
```

---

## 🔄 Set and Dictionary Comprehensions

### Set

```python
unique_lengths = {len(word) for word in ["hello", "world", "hi"]}
```

### Dictionary

```python
squares_dict = {x: x**2 for x in range(1, 6)}
print(squares_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

## 🧪 Challenge Time

Try to solve these using comprehensions:

1. Create a list of the first 10 multiples of 3.
2. Build a set of unique characters (excluding spaces) from a sentence.
3. Create a dictionary that maps numbers from 1 to 5 to their factorial.

---

## 🎯 Why use comprehensions?

* Write cleaner and more expressive code
* Avoid unnecessary boilerplate
* Easier to spot transformations at a glance

But remember: **don’t sacrifice readability for conciseness**. If it becomes too complex, a regular loop might be better.

---

> 🚀 Mastering comprehensions will make your Python code faster to write and easier to read. A small investment for big clarity!

**Next Module [object orientation](../4.%20object_orientation/README.md)**
