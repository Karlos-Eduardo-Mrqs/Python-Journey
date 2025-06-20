# 🟨 Tuples ``(tuple)`` in Python

Tuples are another important data structure in Python. They are very similar to lists, but with a fundamental difference: **they are immutable**, that is, once created, their values **cannot be modified**.

---

## ✅ Creation of tuples

You can create a tuple using brackets `()

```python
# Tuple of fruit
fruits = ("apple", "banana", "orange")

# Mixed tuple
mixture = (1, "text", True, 3.14)
```

> 💡 Tip: Parentheses are optional! You can declare a tuple simply by separating the elements with commas:

```python
numbers = 1, 2, 3
```

---

## 🔎 How to access the items?

Just like in lists, you can access the elements of the tuple by **indexes**, starting from scratch:

```python
print(fruits[0])   # "apple"
print(fruits[-1])   # "orange" (last element)
```

> ✅ Negative indexes also work, just like in lists.

---

## 🚫 Tuples are immutable

As the tuples are **immutable**, trying to modify an element generates an error:

```python
fruits[1] = "grape"  # TypeError
```

**This will generate an error! ** If you need to modify it, convert the tuple into a list:

```python
list_fruits = list(fruits)
list_fruit[1] = "grape"
fruits = tuple(listed fruits)
```

---

## 🧰 Useful methods

Being immutable, tuples have fewer methods than lists. The most used are:

| Method   | Function   |
|-----------|--------------------------------------------------------|
| `index()` | Returns the index of the first value found.   |
| `count()` | Counts how many times a value appears.   |
| `len()`   | Returns the number of items.   |

---

## 💻 Practical examples

🔖 ``index()``

```python
numbers = (10, 20, 30, 20)
print(numbers.index(30))  # Output: 2
```

🔖 ``count()``

```python
numbers = (10, 20, 30, 20)
print(numbers.count(20))  # Output: 2
```

🔖 ``len()``

```python
numbers = (1, 2, 3, 4)
print(len(numbers))  # Output: 4
```

---

## 🔁 Iterating with 'for'

Tuples are iterable, that is, they can be traversed with the loop `for':

```python
colors = ("red", "blue", "green")

for color in colors:
    print(color)
```

Or if you want to show everything in one line:

```python
print(", ".join(colors))  # Output: red, blue, green
```

---

## 📦 Unpacking of tuples

Tuples provide a practical way of assigning values to several variables at once:

```python
point = (10, 20)
x, y = point

print(x)  # 10
print(and)  # 20
```

---

## ✅ Conclusion

Tuples are ideal when you need to store data that **should not be modified**, such as:

- Coordinates;
- Dates;
- Fixed records.

By the end of this content, you will already be able to:

- Create tuples with different types of data;
- Access items with positive and negative indexes;
- Understand the difference between mutability and immutability;
- Use methods such as ``index()``, ``count()`` and ``len()``;
- Walk tuples with the loop for;
- Apply the unpacking of tuples.

> ➡️ Tuples are simple, fast and safe. Knowing when to use them is essential for writing efficient and well-structured code.

Now that you understand the **lists** and the **tuples**, let’s continue with the **sets ('set')** and the **dictionaries ('dict')**. Continues to study! 💪🐍

**Next File [Dictionaries](./dictionaries.md)**