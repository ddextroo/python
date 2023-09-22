
# Python User-Defined Functions Cheat Sheet

## Function Basics

### Defining a Function

```python
def my_function():
    # Function body
    pass
```

### Calling a Function

```python
my_function()  # Call the function
```

### Function Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### Default Parameters

```python
def greet(name="User"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, User!
greet("Alice")  # Output: Hello, Alice!
```

### Return Statement

```python
def add(x, y):
    return x + y

result = add(3, 4)
print(result)  # Output: 7
```

## Scope and Lifetime

### Global vs. Local Variables

```python
x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print(x)  # Access global variable

my_function()  # Output: 10
print(y)       # Error: NameError: name 'y' is not defined
```

## Recursion

### Recursive Function

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(5)
print(result)  # Output: 120
```

## Lambda Functions

### Lambda Function

```python
multiply = lambda x, y: x * y
result = multiply(3, 4)
print(result)  # Output: 12
```

## Function Annotations

### Function Annotations

```python
def add(x: int, y: int) -> int:
    return x + y

result = add(3, 4)
print(result)  # Output: 7
```

## Docstrings

### Function Docstring

```python
def greet(name):
    """
    This function greets the person passed in as a parameter.
    """
    print(f"Hello, {name}!")
```

## Function Overloading

Python does not support function overloading like some other languages.

## Examples

### Example 1: Calculate the Area of a Rectangle

```python
def calculate_area(length, width):
    return length * width

area = calculate_area(5, 4)
print(f"The area is {area} square units.")  # Output: The area is 20 square units.
```

### Example 2: Check if a Number is Even

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(7)
print(result)  # Output: False
```

### Example 3: Find the Maximum of Three Numbers

```python
def find_max(x, y, z):
    max_num = x if x > y else y
    max_num = max_num if max_num > z else z
    return max_num

result = find_max(7, 3, 9)
print(result)  # Output: 9
```

This cheat sheet provides an overview of user-defined functions in Python, including function definition, parameters, return statements, scope, recursion, lambda functions, function annotations, and examples.
```

You can copy and paste this markdown code into a GitHub README or Markdown file.
