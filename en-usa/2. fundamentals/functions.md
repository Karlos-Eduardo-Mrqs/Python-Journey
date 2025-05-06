# 🧰 Functions in Python

Functions are reusable blocks of code that can be called to perform a specific task. They help make the code more organized, modular and easy to understand.

## 📌 Why use functions?

- **Code reuse:** avoids repeating the same code multiple times.
- **Modularization:** organizes the code into logical and independent blocks.
- **Better readability and maintainability:** makes it easier to understand and change the code.

## 🔹 Function declaration with def

To create a function, we use the def keyword, followed by the function name, parentheses, and a colon. The function body is indented.

> ✅ Syntax:

```python
def function_name(parameters):
    # function code
    return value
```

> 📌 Usage example: Simple function that prints a greeting.

```python
def greeting():
    print("Hello, welcome!")

greeting() # Output: Hello, welcome!
```

## 🔷 Parameters and Arguments

Parameters are the variables listed in the function declaration. Arguments are the values ​​passed to the function when it is called.

> 📌 Usage example:

```python
def greeting(name):
    print(f"Hello, {name}!")

greeting("Carlos") # Output: Hello, Carlos!
```

## 🔷 Default and Named Arguments

In Python, we can make parameters optional by assigning them default values. We can also specify values ​​by name, which allows you to change the order of the arguments and increases the readability of the code.

### Parameters with default values

Parameters with default values ​​allow you to define an "automatic" value for a parameter, in case it is not specified in the function call. This makes the parameter optional and avoids errors when calling the function with fewer arguments.

> ✅ Syntax:

```python
def function_name(parameter1=value1, parameter2=value2):
# code
```

> 📌 Usage example:

```python
def greeting(name="User"):
print(f"Hello, {name}!")

greeting() # Output: Hello, User!
greeting("Anna") # Output: Hello, Anna!
```

#### 📘 Explanation

In the example above, the greeting function was defined with a default value of "User" for the name parameter. So, if the user does not pass any arguments, "User" will be used automatically.

### Named Arguments

Named arguments allow you to pass values ​​by specifying the name of the parameter. This makes the function call clearer and allows you to change the order of the arguments without affecting the logic.

> 📌 Usage example:

```python
def greeting(name, age):
print(f"Hello, {name}. You are {age} years old.")

greeting(age=25, name="Carlos") # Output: Hello, Carlos. You are 25 years old.
```

#### 📘 Explanation

Even if age comes before name in the function call, it works correctly because the arguments were named. This is useful for functions with many parameters, or when we want to make the code more readable.

## 🔷 return

The return statement is used to return a value from a function. When a function encounters a return, it ends execution and returns the specified value.

> ✅ Syntax:

```python
def sum(a, b):
return a + b
```

> 📌 Usage example:

```python
def sum(a, b):
return a + b

result = sum(3, 5)
print(result) # Output: 8
```

## 🔷 Functions with Multiple Returns

In Python, a function can return more than one value at once. These values ​​are returned as a tuple (even if you don't see the parentheses) and can be unpacked into separate variables.

> ✅ Syntax

```python
def function_name():
return value1, value2, ..., valueN
```

> 📌 Example explained

```python
def operations(a, b):
sum = a + b
product = a * b
return sum, product # returns two values
```

### 💡 Helpful tip

You can mix positional and named arguments, but the positional arguments must come before the named ones. This ensures clarity in reading and avoids errors when calling the function. Example:

```python
def personal_data(name, age, city="Unknown"):
print(f"Name: {name}, Age: {age}, City: {city}")

personal_data("Ana", 30, city="São Paulo")
```

## 🔹 Variable Scope

A variable's scope determines where it can be accessed. There are two types of scope in Python:

- **Local Scope:🚩** Variables defined inside a function, accessible only inside that function.

- **Global Scope:🌐** Variables defined outside any function, accessible anywhere in the code.

> 📌 Example of scope usage:

```python
global_variable = "I'm global!"

def example():
local_variable = "I'm local!"
print(global_variable) # Access the global variable
print(local_variable) # Access the local variable

example()
# print(local_variable) # Error! Cannot access local variables outside the function. ```

## 🔷 Anonymous Functions with Lambda

Anonymous functions, or lambda functions, are small, unnamed functions that are usually used for simple operations that can be done in a single line. They are very useful in functions such as map(), filter(), and sorted().

> ✅ Syntax:

```python
variable = lambda arguments: expression
```

> 📌 Usage example:

```python
sum = lambda x, y: x + y
print(sum(3, 5)) # Output: 8
```

## Conclusion 🚀

Python functions are reusable blocks of code that allow you to organize and modularize your program, making it more readable, efficient, and maintainable. They are essential for reducing code repetition and making it easier to create scalable programs.

By understanding how to define and call functions, how to pass parameters and return values, you will be able to create more sophisticated and elegant solutions. In addition, functions can have default parameters, variables, and return multiple values, which further increases their flexibility.

## 📝 Function Exercises

1. **Sum Function**
Create a function that receives two numbers as parameters and returns their sum.

2. **Average Function**
Create a function that receives a list of numbers and returns the average of these numbers.

3. **Factorial Function**
Implement a function that calculates the factorial of a number.

4. **Prime Number Checking Function**
Create a function that determines whether a given number is prime.

5. **Character Counting Function**
Create a function that counts the number of occurrences of a character in a string.

## 🔧 Tips for practice:

- **Code modularization:**
Divide your code into small functions, each responsible for a specific task, to facilitate maintenance and reuse.

- **Recursive functions:**
Try creating recursive functions for problems that can be broken down into smaller subproblems, such as calculating factorial or solving search and sort problems.

> Now it's time to put your learning into practice! ✨🐍 Keep exploring and creating your own functions to solve everyday problems and improve your Python skills!
