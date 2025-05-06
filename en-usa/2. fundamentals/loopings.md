# ⚙️ Repetition Structures in Python

Repetition structures allow a block of code to be executed multiple times, based on a condition or a specific number of iterations. They are essential for automating repetitive tasks and processing large volumes of data efficiently.

## 📌 Why are they important?

- They allow you to automate repetitive tasks;
- They facilitate the processing of data collections;
- They make the code more compact and easier to understand;

## 🔷 Main types of repetition

### 🔹 for

The for structure is used to iterate over a sequence (such as a list, tuple, string or range of numbers). It is ideal for when you know the number of iterations you want to perform.

> ✅ Syntax:

```python
for item in sequence:
# code block
```

> 📌 Usage example: Iterate over a list of numbers and print each one.

```python
numbers = [1, 2, 3, 4, 5]
for number in numbers:
print(number)
```

### 🔷 while

The while structure executes a block of code while a condition is true. It is useful when the number of iterations is not known in advance.

> ✅ Syntax:

```python
while condition:
# code block
```

> 📌 Usage example: Printing numbers from 1 to 5 with while.

```python
counter = 1
while counter <= 5:
print(counter)
counter += 1
```

## 🔹 break, continue, and pass

These statements change the default behavior of loops like for and while.

### 🔸 break

The break statement is used to stop a loop prematurely. When Python encounters a break, it immediately exits the loop and continues executing the code after the loop.

> 📌 Example of use with break:

```python
number = 0
for number in range(10):
print(number) # 0, 1 , 2 , 3 , 4 , 5
if number == 5:
break # Stops the loop when the number is 5
print(number)
```

### 🔸 continue

The continue statement causes the loop to skip the current iteration and go directly to the next iteration, without executing the rest of the code inside the loop for the current iteration.

> 📌 Example of use with continue:

```python
number = 0
for number in range(10):
print(number) # 0 , 1 , 2 , 3 , 4 , 6 , 7 , 8, 9
if number == 5:
continue # Skip the iteration when the number is 5
print(number)

```

### 🔸 pass

The pass statement is a placeholder. It is useful when you need a control structure, such as an if or a loop, but you don't want anything to happen inside that structure, or if you are developing the code and want to leave a part open without errors.

> 📌 Example of use with pass:

```python
number = 0
for number in range(5):
print(number) # 0 , 1 , 2 , 3 , 4
if number == 3:
pass # Do nothing when number is 3
print(number)
```

## 🔷 Iteration Functions

### 🔹 range()

The range() function is used to generate a sequence of numbers, very useful in for loops. It can receive up to three arguments: start, stop and step.

> ✅ Syntax:

```python
start:1 # starting value (inclusive).
stop: 10 # ending value (exclusive).
step: 1 # increment value (optional).

range(start, stop, step)
```

> 📌 Usage example with range(): Create a sequence of numbers from 0 to 9.

```python
for i in range(10):
print(i)
📌 Usage example with range(): Create a sequence with an increment of 2.
```

```python
for i in range(0, 10, 2):
print(i)
```

### 🔹 enumerate()

The enumerate() function adds an automatic counter to an iterable, returning a tuple with the index and value.

> ✅ Syntax:

```python
enumerate(iterable)
```

> 📌 Usage example with enumerate(): Iterate over a list and get the index and value.

```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
print(f"Index {index}: {fruit}")
```

### 🔹 zip()

The zip() function combines two or more iterables, returning a sequence of tuples. Each tuple contains the corresponding elements of the iterables.

> ✅ Syntax:

```python
zip(iterable1, iterable2, ...)
```

> 📌 Example of using zip(): Combine two lists and iterate over them.

```python
names = ["John", "Mary", "Carlos"]
ages = [25, 30, 22]
for name, age in zip(names, ages):
print(f"{name} is {age} years old")
```

### 🔹 List Comprehensions

List comprehensions provide a compact and efficient way to create lists from other collections or sequences, using a simpler syntax than traditional loops. In addition, it is especially useful when you want to apply a simple transformation to each element of a list or filter them with a condition.

> ✅ Syntax:

```python
[expression for item in iterable if condition]
```

> 📌 Usage example:

```python
numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares) # Output: [1, 4, 9, 16, 25]
```

---

## 🚀 Conclusion

Repetition structures are essential for automating tasks and working with large volumes of data in Python. With them, you can repeat actions based on conditions (`while`) or efficiently traverse sequences (`for`), in addition to controlling the flow of execution with `break`, `continue` and `pass`.

By also mastering tools such as `range()`, `enumerate()`, `zip()` and list comprehensions, you make your code cleaner, more elegant and more powerful.

## 📝 Repetition Exercises

1. **Counting from 1 to 10 using `for`**
Create a program that uses a `for` loop to print the numbers from 1 to 10.

2. **Counter with `while`**
Make a program that counts from 0 to 20, skipping 2 by 2, using `while`.

3. **Sum of a list**
Use a `for` to add all the elements of a list of integers.

4. **Search with `break`**
Create a program that receives a list and stops going through it as soon as it finds the number 0.

5. **Filtering pairs with `continue`**
Go through a list and print only the even numbers, using `continue` to ignore the odd ones.

6. **List comprehension**
Create a new list with the squares of the numbers 1 to 10 using list comprehension.

## 🔧 Tips for practice:

- **Use `for` when you know how many times you need to repeat something.**
- **Use `while` when the repetition depends on a condition.**
- **Explore functions like `range()`, `enumerate()` and `zip()` to make your loops more powerful.**
- **Practice reading and writing list comprehensions — they make your code leaner and more expressive.**

> Now it's your turn! 🐍 Practice with the exercises, try variations of the examples and continue evolving in the world of programming with Python!
