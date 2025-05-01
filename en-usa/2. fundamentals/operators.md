# 🔢 Operators in Python

Operators are symbols used to perform operations on variables and values. Python has several types of operators.

## 🔹 Arithmetic ➕➖✖️➗

> **Arithmetic operators are used to perform mathematical operations, such as adding, subtracting, multiplying, and dividing values.**

> They are useful in any situation where calculations need to be made — whether it's adding the age of users, calculating discounts, or multiplying values ​​in a shopping cart.

| 🧮 Operator | 📝 Description | 💡 Example |
|------------|--------------|------------|
| `+` | Addition | `2 + 3` → `5` |
| `-` | Subtraction | `5 - 2` → `3` |
| `*` | Multiplication | `4 * 2` → `8` |
| `/` | Division | `10 / 2` → `5.0` |
| `//` | Integer division | `10 // 3` → `3` |
| `%` | Modulus (remainder) | `10 % 3` → `1` |
| `**` | Power | `2 ** 3` → `8` |

## 🔹 Relational (Comparison) 🔎

> **These operators compare two values ​​and return a boolean result (``True`` or ``False``).** 

> They are essential in decision structures, such as ``if``, as they help us know if something is greater than, less than, equal to or different from another value.

| 🔁 Operator | 🤔 Meaning | 💡 Example |
|------------|----------------|------------|
| `==` | Equal | `5 == 5` → `True` |
| `!=` | Not equal | `5 != 3` → `True` |
| `>` | Greater than | `4 > 2` → `True` |
| `<` | Less than | `2 < 1` → `False` |
| `>=` | Greater than or equal | `4 >= 4` → `True` |
| `<=` | Less than or equal | `3 <= 5` → `True` |

## 🔹 Logical 🔗

> **Logical operators are used to combine boolean expressions.**

> They are very useful when we want to check multiple conditions at the same time. For example: checking if a user is logged in and has administrator permissions.

### 📘 Truth Table

> **A truth table shows all possible combinations of logical values ​​(True or False) for a given operation.**

> It is essential to understand the behavior of operators such as and, or and not.

| A | B | A and B | A or B | not A |
|---|---|----------|---------|--------|
| ✅ | ✅ | ✅ | ✅ | ❌ |
| ✅ | ❌ | ❌ | ✅ | ❌ |
| ❌ | ✅ | ❌ | ✅ | ✅ |
| ❌ | ❌ | ❌ | ❌ | ✅ |

> **✅: ``True`` | ❌: ``False``**

### 🔹 Examples 🔗

| 🔣 Operator | 💬 Example | 🎯 Result |
|-------------|------------|--------------|
| `and` | `True and False` | `False` |
| `or` | `True or False` | `True` |
| `not` | `not True` | `False` |

**Tip🔎:**

- ``and`` -> only returns True if both are ``True``.
- ``or`` -> returns ``True`` if at least one is ``True``.
- ``not`` -> 🔁 inverts the value

> 📌 The `not` operator only depends on one (unary) value, unlike `and` and `or`, which compare two values.

## 🔹 Identity Operators 🆔

> Used to check if two variables point to the same object in memory, and not just if they have the same value.

| Operator | Description | Example | Result |
|----------|-----------|----------|-----------|
| `is` | Returns `True` if the variables reference the same object in memory | `a is b` | `True` or `False` |
| `is not` | Returns `True` if the objects are **different** | `a is not b` | `True` or `False` |

> **💡 Hint: a == b compares the values, while a is b compares if they are the same object in memory.**

### Example 🆔

```python
a = [1, 2]
b = a
c = [1, 2]
print(a is b) # True → a and b are the same object
print(a is c) # False → a and c have the same content, but are different objects
```

## 🔹 Membership Operators 🔎📦

> Used to test if a value exists within a sequence, such as lists, strings or dictionaries.

| Operator | Description | Example | Result |
|----------|----------|---------|----------|
| `in` | Returns `True` if the value is present | `'a' in 'Carlos'` | `True` |
| `not in` | Returns `True` if the value is **not** present | `5 not in [1,2,3]` | `True` |

### Example 🔎📦

```python
fruits = ['apple', 'banana']
print('banana' in fruits) # True
print('orange' not in fruits) # True
print("grape" in fruits) # False
```
## 🔹 Bitwise Operators 🧠⚙️

> Operate directly on bits, being useful in low-level programming, networks, cryptography or manipulation of binary permissions.

| 🔢 Operator | 📛 Name | 💬 Description |
|-------------|---------|---------------|
| `&` | AND | Returns 1 if **both** bits are 1 |
| `|` | OR | Returns 1 if **any** bit is 1 |
| `^` | XOR | Returns 1 if bits are **different** |
| `~` | NOT | Inverts all bits |
| `<<` | Left shift | Shifts bits to the left |
| `>>` | Right shift | Shifts bits to the right |

### Example 🧠⚙️

```python
a = 5 # binary: 0101
b = 3 # binary: 0011
print(a & b) # 1 → 0001 (0101 & 0011)
print(a | b) # 7 → 0111 (0101 | 0011)
```

## 🔹 Assignment 📝

> **They are used to store values ​​in variables.** In addition to the classic ``=``, there are operators that perform an operation and update the value of the variable, such as ``+=``, ``-=``, etc. This makes the code cleaner and more direct.

| 🔢 Operator | 🟰 Equivalent |
|----------|-------------|
| `=` | Simple assignment |
| `+=` | Adds and assigns |
| `-=` | Subtracts and assigns |
| `*=` | Multiplies and assigns |
| `/=` | Divides and assigns |
| `//=` | Performs integer division and assigns |
| `%=` | Performs the modulus (remainder) and assigns |
| `**=` | Performs exponentiation and assigns |

---

## ⚖️ Operator Precedence

The order Python uses to resolve expressions:

1. `()` Parentheses
2. `**` Exponentiation
3. `+`, `-` (unary)
4. `*`, `/`, `//`, `%`
5. `+`, `-` (binary)
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. `==`, `!=`, `>`, `<`, `>=`, `<=`, `is`, `in`
11. `not`
12. `and`
13. `or`
14. `=`, `+=`, `-=`, etc.

---