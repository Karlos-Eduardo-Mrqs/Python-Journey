# ⚙️ Conditional Structures in Python

Conditional structures allow your code to make decisions based on specific conditions. This way, you can create programs that behave differently depending on the inputs and situations.

## 📌 Why are they important?

- Check values ​​and execute specific commands;
- Define different execution flows;
- Create validations and data processing;
- Improve the logic and dynamics of the program;

## 🔷 Main types of conditionals

### 🔹 if, elif and else

The most basic and common structure for making decisions in Python. It allows you to execute different blocks of code based on one or more conditions.

> ✅ Syntax:

```python
if condition1:
# code block if condition1 is true
elif condition2:
# code block if condition1 is false and condition2 is true
else:
# code block if all previous conditions are false
```

> 📌 Usage example: Check if a number is positive, negative or zero.

```python
if number > 0:
print("Positive number")
elif number < 0:
print("Negative number")
else:
print("Zero")
```

### 🔹 Nested Conditionals

They are if structures within other if structures. They allow you to check dependent or hierarchical conditions, deepening the decision logic.

> ✅ Syntax:

```python
if condition1:
    if condition2:
        # block if both conditions are true
    else:
        # block if condition1 is true and condition2 is false
else:
    # block if condition1 is false
```

> 📌 Usage example: Validate two linked conditions, such as grade and attendance.

```python
if grade >= 7: # If the grade is greater than or equal to seven, advance in the algorithm
    if frequency >= 75: # If the frequency is greater than or equal to 75%, it will be approved
        print("Approved")
    else:
        print("Failed due to attendance")
else:
    print("Failed by grade")
```

### 🔹 Ternary Operator

A compact way to write simple conditions in a single line. Ideal when you want to assign values ​​or return short expressions in an elegant way.

> ✅ Syntax:

```python
value_if_true if condition else value_if_false 
```

> 📌 Usage example:

```python
status = "Approved" if grade >= 7 else "Failed" # If the grade is greater than or equal to seven, the status will be approved, otherwise the status will be failed
```

### 🔹 Match case (valid in Python 3.10+)

It is the structure introduced in Python 3.10 to replace the switch in other languages. Allows you to compare a value with multiple "cases", making the code cleaner and more organized for multiple decisions based on the same value.

> ✅ Syntax:

```python
match variable:
    case value1:
        # code block for value1
    case value2:
        # code block for value2
    case_:
        # default block (equivalent to "default")
```

**The _ (underscore) character represents the "default" case, which will be executed if none of the above are satisfied.**

> 📌 Usage example:

```python
color = "red"

match color:
    case "red":
        print("Chosen color: Red")
    case "blue":
        print("Chosen color: Blue")
    case "green":
        print("Chosen color: Green")
    case_:
        print("Unrecognized color")
```

---

## 🚀 Conclusion

Conditional statements in Python are powerful tools that allow your code to make decisions based on dynamic conditions.

They are essential for controlling the flow of your program, making it flexible and adaptable to different inputs and situations. By understanding how to use if, elif, else, nested conditional statements, the ternary operator, and match case, you will have a robust set of tools to handle any type of conditional situation.

### 📝 Conditional Exercises

1. **Check if the number is positive, negative or zero.**
Implement a program that reads a number and prints whether it is positive, negative or zero.

2. **Age classification**
Create a program that reads a person's age and classifies them as:

- Child (0 to 12 years old)
- Teenager (13 to 17 years old)
- Adult (18 to 64 years old)
- Elderly (65 years old or older)

3. **Grade verification**

Make a program that reads a grade from 0 to 10 and informs whether the student passed, failed or is recovering. The criteria are:

- Approved: grade >= 7
- Recovered: 5 <= grade < 7
- Failed: grade < 5

4. **Simple calculator**

Create a program that reads two numbers and a mathematical operator (+, -, *, /). The program must perform the corresponding operation between the two numbers and display the result.

5. **Greater than three numbers**

Create a program that reads three numbers and prints the largest number among them, using conditional structures.

## 🔧 Tips for practice

- **Validation of user input:**
Use conditionals to validate data inputs, such as discount calculations based on age or customer category.

- **Multiple cases:**
Use match case for systems that involve multiple cases, making your code more organized and readable.

> Now it's time to put your learning into practice! ✨🐍 Keep exploring, solving challenges and improving your Python skills!

**Next file [loopings](03_loopings.md)**
