
# Python Object & Class Cheat Sheet

## Classes and Objects

**Class Definition**

```python
class MyClass:
    # Class attributes and methods
    pass
```

**Creating Objects**

```python
obj = MyClass()  # Create an instance of MyClass
```

**Constructor Method**

```python
class MyClass:
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2
```

**Instance Variables**

```python
obj = MyClass("value1", "value2")
print(obj.param1)  # Access instance variable
```

## Methods

**Instance Methods**

```python
class MyClass:
    def my_method(self):
        # Access instance variables and perform actions
        pass

obj = MyClass()
obj.my_method()
```

**Class Methods**

```python
class MyClass:
    @classmethod
    def my_class_method(cls):
        # Access class-level attributes and perform actions
        pass

MyClass.my_class_method()
```

## Inheritance

**Base Class (Superclass)**

```python
class ParentClass:
    # Attributes and methods

class ChildClass(ParentClass):
    # Attributes and methods
```

**Method Overriding**

```python
class ParentClass:
    def my_method(self):
        return "Parent method"

class ChildClass(ParentClass):
    def my_method(self):
        return "Child method"

child_obj = ChildClass()
print(child_obj.my_method())  # Output: "Child method"
```

## Encapsulation

**Private Variables**

```python
class MyClass:
    def __init__(self):
        self.__private_var = 42

    def get_private_var(self):
        return self.__private_var

obj = MyClass()
print(obj.get_private_var())  # Access private variable
```

## Polymorphism

**Duck Typing**

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_speak(dog))  # Output: "Woof!"
print(animal_speak(cat))  # Output: "Meow!"
```

## Examples

**Example 1: Creating a Student Class**

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

student = Student("Alice", 20)
print(student.display_info())  # Output: "Name: Alice, Age: 20"
```

***Example 2: Inheritance with Shape Classes**

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle = Rectangle(5, 4)
print(rectangle.area())  # Output: 20
```

**Example 3: Polymorphism with Animal Classes**

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_speak(dog))  # Output: "Woof!"
print(animal_speak(cat))  # Output: "Meow!"
```

