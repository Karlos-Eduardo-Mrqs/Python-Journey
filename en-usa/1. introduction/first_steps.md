# First Steps
Now that the environment has been previously configured, we can begin our first steps with Python programming!

# Variables
Variables are used to store information that can be manipulated throughout the program. In Python, creating a variable is simple and does not require defining the data type (as occurs in other languages, Java or C++).

# 🧠 Rules for Naming Variables

| Rule | Description |
|:------|:----------|
| Start with a letter or `_` | The variable name must start with a letter (a-z, A-Z) or an underscore (`_`). |
| Letters, numbers and underscores | After the first character, the name can contain letters, numbers and underscores. |
| Do not start with a number | Variables **cannot** start with numbers. |
| Case-sensitive | Python is case-sensitive (`name`, `Name` and `NAME` are different variables). |
| Avoid reserved words | Do not use language keywords (such as `class`, `if`, `for`) as variable names. |

> Best practices: use descriptive names that make it clear what the variable represents.


# ✅ Variable Name Examples

| Name | Type | Note |
|:-----|:--------|:-----------|
| name | Valid | Lowercase letters only. |
| for | Invalid | `for` is a reserved word in Python. |
| Full_Name | Valid | Use of uppercase letters and underscore. |
| age29 | Valid | Can have numbers, but **not at the beginning**. |
| class | Invalid | `class` is a reserved word in Python. |
| _address | Valid | Starting with an underscore is allowed. |
| 29age | Invalid | Cannot start with a number. |
| fullname | Invalid | Spaces are not allowed; use `_`. |

# Data Types
In Python, data types determine the type of value a variable can store. Python is a dynamically typed language, which means you don't need to declare the type of the variable explicitly.

# 🔹 Python Data Types Table

| Data Type | Description | Code Example | Real Life Example |
|:-------------|:----------|:------------------|:--------------------|
| **int** | Integers (no decimal places). | `age = 30` | Age of a person: `30 years old` |
| **float** | Numbers with decimal places. | `height = 1.75` | Height of a person: `1.75 meters` |
| **str** | Strings (text). | `name = "Carlos"` | Name of a student: `"Carlos"` |
| **bool** | Boolean values ​​(`True` or `False`). | `is_student = True` | Whether the person is enrolled: `True` |
| **list** | Ordered and mutable collections. | `fruits = ["apple", "banana", "orange"]` | Grocery shopping list. |
| **tuple** | Ordered and immutable collections. | `coordinates = (10, 20)` | GPS location: `(latitude, longitude)` |
| **dict** | Collections of key-value pairs. | `student = {"name": "Carlos", "age": 20}` | Student registration form. |

# 📚 Quick Explanation
    
- **Integers (int):** Used to count, identify or enumerate.

- **Floats (float):** Represent fractional values, such as heights and measurements.

- **Strings (str):** Are texts that can include letters, numbers and symbols.

- **Booleans (bool):** Represent only two states: true or false.

- **Lists (list):** Store a sequence of values ​​that can be changed.

- **Tuples (tuple):** Store a sequence that cannot be changed.

- **Dictionaries (dict):** Store data in pairs (key and value), like an information sheet.

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

# Input and Output Commands
Now that you understand variables and data types, let's learn how to interact with the user!

Python has simple functions for data input and output:

---

## 🔹 Output: `print()`

The `print()` command is used to display information on the console.

### Examples:
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

### Example:

```python
name = input("Enter your name: ")
print("Welcome,", name)
```

> How it works:

The program will pause and wait for the user to type something.

Everything that is typed will be stored as a string.

## ⚡ Attention!
By default, whatever is read by input() will be of type str (text), even if the user enters numbers!

**To convert the type, we use casting:**

Conversion example:

```python
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
```

- **int() :** converts to integer.
- **float() :** converts to floating point.

---

# 🚀 Conclusion

These first steps are essential for your journey with the Python language. From here, you can already build small scripts that receive user data, process information and display results on the screen.

> Keep practicing! Try:

- Create a program that calculates the average of two grades;
- Make a simple registration with name, age and city;
- Develop a dictionary that has name, age, situation (studying: true), and others;

> Each small exercise will make you more confident and prepared for the next modules — such as conditional structures, repetitions, functions and much more! 💡🐍