# 🟩 Lists (`list`) in Python

Lists are one of the most commonly used data structures in Python. They store **ordered** collections of elements and can be modified at any time.

## ✅ Creating lists

You can create a list using square brackets `[]` and separating the elements with commas.

```python
# List of fruits
fruits = ["apple", "banana", "orange"]

# Mixed list
mix = [1, "text", True, 3.14]
```

## 🔍 How to access the elements?

```python
print(fruits[0])    # 'apple'
print(fruits[-1])   # "orange" (last element)
```

## ✏️ How to change an element

```python
fruits[1] = "grape"
print(fruits)  # ["apple", "grape", "orange"]
```

## 🧰 Most commonly used methods

| Method      | What it does                             |
| ----------- | ------------------------------------- |
| `append()`  | Adds an element to the end of the list    |
| `insert()`  | Inserts an element at a position         |
| `remove()`  | Removes the first occurrence of the value |
| `pop()`     | Removes and returns the element by index      |
| `clear()`   | Removes all elements from the list        |
| `sort()`    | Sorts the elements in the list              |
| `reverse()` | Reverses the order of the list              |
| `len()`     | Returns the number of elements             |

### 💻 Practical examples

> 🔖 ``append()``

```python
fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  # ["apple", "banana", "orange"]
```

> 🔖 ``insert()``

```python
fruits = ["apple", "orange"]
fruits.insert(1, "banana")
print(fruits)  # ["apple", "banana", "orange"]
```

> 🔖 ``remove()``

```python
fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)  # ["apple", "orange"]
```

> 🔖 ``pop()``

```python
fruits = ["apple", "banana", "orange"]
item = fruits.pop(1)
print(item)    # "banana"
print(fruits)  # ["apple", "orange"]
```

> 🔖 ``clear()``

```python
fruits = ["apple", "banana", "orange"]
fruits.clear()
print(fruits)  # []
```

> 🔖 ``sort()``

```python
fruits = ["banana", "apple", "orange"]
fruits.sort()
print(fruits)  # ["banana", "orange", "apple"]
```

> 🔖 ``reverse()``

```python
fruits = ["banana", "apple", "orange"]
fruits.reverse()
print(fruits)  # ["orange", "apple", "banana"]

> 🔖 ``len()``

```python
fruits = ["apple", "banana", "orange"]
print(len(fruits))  # 3
```

### 🔁 How to use for with lists

You can iterate over all the elements in a list using a for loop.

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit) # apple, banana, orange 

```

---

# ✅ Conclusion

Lists are one of the pillars of Python programming. They allow you to store, organize, and manipulate collections of data in an easy and powerful way.

After this section, you will be able to:

- Create lists with different types of data;
- Access and modify elements;
- Use useful methods such as append(), pop(), sort(), and many others;
- Iterate through lists with for;
- Solve practical challenges with lists!

> ➡️ Mastering lists is essential to continue with more advanced topics such as repetition structures, functions, and even file and data manipulation.
> Now that you are familiar with this structure, try creating your own programs with lists and see how they can make your life as a Python programmer easier. 💡🐍

## 🧪 Challenge!

Try it yourself:

1. Create a list with 5 names.
2. Sort the list.
3. Remove the third name.
4. Add 2 new names.
5. Display the final result with print().