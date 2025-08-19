# 🟨 Dictionaries (`dict`) in Python

## 📌 What Is?

A **dictionary** is a dice structure that assembles pairs of **key → value**. It is a **mutável** collection, **unordered** (Até or Python 3.6) and **indexed by key**, not by position.

```python
# Dictionary example
aluno = {"nome": "Carlos", "idade": 20, "course": "Python"}
print(aluno["name"]) # output: Carlos
```

## 🔑 Key Features

* As **keys are only unique**.
* The **values ​​can be of any type**.
* As keys they are normally `str`, `int`, or `tuple` immutáveis.

## 🧰 Main methods and operations

| Method | Description |
| ----------- | -------------------------------------------------- |
| `dict[key]` | Accesses the value of the key `key`. |
| `get(key)` | Returns the value of the key or `None` does not exist. |
| `keys()` | Returns all keys. |
| `values()` | Returns all values. |
| `items()` | Returns the (key, value) pairs. |
| `update()` | Updates with new pairs. |
| `pop(key)` | Removes the pair with the given key. |

### 🧪 Practical example

```python
book = {
"title": "Basic Python",
"author": "João Silva",
"year": 2025
}

# Access the book title
print(book["title"])

# Add a new pair, number of pages
book["pages"] = 300

# Update the year value
book["year"] = 2024

# Iterate over the dictionary
for key, value in book.items():
print(f"{key}: {value}")
```

## ✅ When to use?

* When you need to associate a given item with a significant key.
* To store an object's attributes, as in a land registry.

---

## 📝 Conclusion

Now that you understand how dictionaries work in Python, it's time to practice!

✅ **Suggested Challenges:**

1. Create a dictionary representing a movie, with information such as title, director, year, and genre.
2. Update the values, add new pairs, and delete a key.
3. Sort through the items with a for and display all the information in a formatted form.

> Practicing is the best way to consolidate your learning! Try different combinations, explore the methods, and use print() to observe the results.

**Next file [Set](04_set.md)**
