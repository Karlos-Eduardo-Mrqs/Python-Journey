# 🟥 Sets (`set`) in Python

## 📌 What Is?

A **set** in Python is an **unordered** collection, **immutável (individually)** and **simply duplicate elements**. Ideal for performing mathematical operations such as union, intersection and difference.

```python
# Set example
numbers = {1, 2, 3, 2, 1}
print(numbers) # said: {1, 2, 3}
```

## 🔑 Key Features

* **No order possible** → It is not possible to access elements by index.
* **Automatically remove duplicates**.
* Elements must be **imutáveis** (`int`, `str`, `tuple`, etc.).

## 🧰 Main methods and operations

| Method | Description |
| -------------------- | --------------------------------------- |
| `add(x)` | Adds an element. |
| `remove(x)` | Deletes `x` if it exists (error if it doesn't exist). |
| `discard(x)` | Deletes `x` without error if it doesn't exist. |
| `union(set2)` | Union of two sets. |
| `intersection(set2)` | Common elements. |
| `difference(set2)` | Elements that do exist at the first time. |
| `issubset(set2)` | Verifies that it is a subset. |
| `issuperset(set2)` | Verifies that it is a superset. |

### 🧪 Practical Example

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b) # Union → {1, 2, 3, 4, 5, 6}
print(a & b) # Intersection → {3, 4}
print(a - b) # Difference → {1, 2}
```

## ✅ When to use?

* To remove **duplicate elements** from a list.
* When you want to perform **mathematical operations on sets**.
* When ordering the elements doesn't matter and you need **high performance in your searches**.

---

## 📝 Conclusion

Now that you've learned about sets in Python, it's time to test your knowledge!

✅ **Suggested challenges:**

1. Create two sets representing presence lists of two classes and calculate:

* Please appear in both turns (intersection).
* Quem appearedeceu barely em uma das turmas (difference).
* The total number of unique students present (união).

2. Use `add()` to insert new alls into the presence lists and `remove()` to correct other options.

3. Experiment with the `issubset()` and `issuperset()` methods:

* Cry a set `turma_A_manha = {"Carlos", "Ana"}`
* A group cries `todos_manha = {"Carlos", "Ana", "Pedro"}`
* Check that `turma_A_manha` is a subset of `all_manha` with `issubset()`
* Check that `todos_manha` is a superset of `turma_A_manha` with `issuperset()`

> Practicing with day-to-day situations helps you better understand the real use of this powerful structure.

---

**Next Module [object orientation](../4.%20object_orientation/README.md) or go to [bonus](./bonus.md)**