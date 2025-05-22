# First Steps 🐍

Now that you have set up your environment, we can start our first steps with Python programming!

---

## 📦 Variables

Variables are used to store information that can be manipulated throughout the program. In Python, creating a variable is simple and does not require defining the data type (as occurs in languages ​​such as Java or C++).

---

## 🧠 Rules for Naming Variables

| Rule | Description |
| :---------------------------- | :----------------------------------------------------------------------------------- |
| Start with a letter or `_` | The name must start with a letter (a-z, A-Z) or an underscore (`_`). |
| Letters, numbers, and underscores | After the first character, it can contain letters, numbers, and underscores. |
| Do not start with a number | Variables **cannot** start with numbers. |
| Case-sensitive | Python is case-sensitive (`name`, `Name`, and `NAME` are different). |
| Avoid reserved words | Do not use language keywords (such as `class`, `if`, `for`). |

> **💡 Good practices:** Use descriptive names that make it clear what the variable represents.

---

## ✅ Examples of Variable Names

| Name | Type | Note |
| :------------- | :------- | :----------------------------------- |
| name | Valid | Lowercase letters only. |
| for | Invalid | Reserved word. |
| Full Name | Valid | Use of uppercase and underscore. |
| age29 | Valid | May contain numbers (not at the beginning). |
| class | Invalid | Reserved word. |
| \_address | Valid | Starting with underscore is allowed. |
| 29age | Invalid | Cannot start with a number. |
| full name | Invalid | Spaces are not allowed; use `_`. |

---

## 🔢 Data Types

Python is a dynamically typed language. This means that you don't need to explicitly declare the type of a variable — it is automatically defined based on the value assigned.

---

### 📋 Data Types Table

| Type | Description | Code Example | Real Example |
| :------ | :------------------------- | :---------------------------------------- | :------------------------------------------------------------ |
| `int` | Integers. | `age = 30` | Age of a person. |
| `float` | Numbers with decimals. | `height = 1.75` | Height in meters. |
| `str` | Text string. | `name = "Carlos"` | Someone's name. |
| `bool` | True or false. | `active = True` | Is it active? |
| `list` | Ordered and mutable list. | `fruits = ["apple", "banana"]` | Shopping list. |
| `tuple` | Ordered and immutable list. | `coordinates = (10, 20)` | GPS location. *(“Tuple” is the English term for “tuple”)* |
| `dict` | Key-value structure. | `student = {"name": "Ana", "age": 20,}` | Student registration. |

---

### 📚 Quick Explanation

- **`int`** → integers.
- **`float`** → decimals.
- **`str`** → texts (strings).
- **`bool`** → logical values ​​(True or False).
- **`list`** → mutable collections.
- **`tuple`** → immutable collections.
- **`dict`** → key and value (dictionary type).

---


## ✅ Combined Practical Example

```python
name = "Ana" # str
age = 25 # int
height = 1.68 # float
student = True # bool
subjects = ["Python", "SQL", "Git"] # list
coordinates = (34.5, -120.7) # tuple
profile = {"name": "Ana", "age": 25} # dict
```

## Input and Output Commands

Let's learn how to interact with the user through data input (``input``) and output (``print``).

---

## 🔹 Data Output: `print()`

The `print()` command is used to display information on the console.

> Start:

```python
print("Hello, world!")
print("The sum of 2 + 3 is:", 2 + 3)
```

> Output:

```bash
Hello, world!
The sum of 2 + 3 is: 5
```

## 🔹 Input: `input()`

The `input()` command allows you to receive data from the user.

> Example:

```python
name = input("Enter your name: ")
print("Welcome", name)
```

> The program will pause and wait for the user to type something.

> Everything that is typed will be stored as a string.

## ⚡ Type Conversion (Casting)

To work with numbers, we need to convert the input manually using casting functions:

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

- **int() :** converts to integer.
- **float() :** converts to floating point.
- **str() :** converts to text (string), if necessary.

---

## 🚀 Conclusion

These first steps are fundamental in your journey with the Python language. From here, you can already build small scripts that receive data, process information and display results on the screen!

> Keep practicing! Try:

- Create a program that calculates the average of two grades;
- Make a simple registration with name, age and city;
- Develop a dictionary that contains names, ages, situations (studying: true), and more;

> 💾 Tip: save your tests in a file like exercicios.py to build your own study base!

> Each small exercise will make you more confident and prepared for the next modules — such as conditional structures, repetitions, functions, and much more! 💡🐍

**Next Module: [Language Fundamentals](../2.%20fundamentals/readme.md)**