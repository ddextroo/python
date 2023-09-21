Certainly! Here are the example codes and their corresponding outputs formatted in GitHub-flavored Markdown (GFM):

**1. String Length:**
```python
my_string = "Hello, World!"
length = len(my_string)
print(length)  # Output: 13
```

**2. Accessing Characters:**
```python
my_string = "Hello, World!"
char = my_string[0]
print(char)  # Output: "H"
```

**3. Slicing Strings:**
```python
my_string = "Hello, World!"
substring = my_string[0:5]
print(substring)  # Output: "Hello"
```

**4. String Concatenation:**
```python
string1 = "Hello, "
string2 = "World!"
new_string = string1 + string2
print(new_string)  # Output: "Hello, World!"
```

**5. Modifying Strings (Creating a New Modified String):**
```python
my_string = "Hello, World!"
new_string = my_string.replace("World", "Python")
print(new_string)  # Output: "Hello, Python!"
```

**6. Checking for Substrings:**
```python
my_string = "Hello, World!"
if "Hello" in my_string:
    print("Found 'Hello'")  # Output: "Found 'Hello'"
```

**7. Changing Case:**
```python
my_string = "Hello, World!"
uppercase_string = my_string.upper()
print(uppercase_string)  # Output: "HELLO, WORLD!"

lowercase_string = my_string.lower()
print(lowercase_string)  # Output: "hello, world!"

titlecase_string = my_string.title()
print(titlecase_string)  # Output: "Hello, World!"
```

**8. Stripping Whitespace:**
```python
my_string = "   Hello, World!   "
stripped_string = my_string.strip()
print(stripped_string)  # Output: "Hello, World!"

left_stripped = my_string.lstrip()
print(left_stripped)  # Output: "Hello, World!   "

right_stripped = my_string.rstrip()
print(right_stripped)  # Output: "   Hello, World!"
```

**9. Splitting and Joining Strings:**
```python
my_string = "apple,banana,orange"
my_list = my_string.split(",")
print(my_list)  # Output: ['apple', 'banana', 'orange']

separator = "-"
new_string = separator.join(my_list)
print(new_string)  # Output: "apple-banana-orange"
```

**10. Reversing Strings:**
```python
my_string = "Hello, World!"
reversed_string = my_string[::-1]
print(reversed_string)  # Output: "!dlroW ,olleH"
```

These examples are now formatted in GitHub-flavored Markdown (GFM) for better readability.
