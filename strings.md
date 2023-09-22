
```markdown
# Python Strings Cheatsheet
```
## Creating Strings


1. **Double Quotes:**
   ```python
   my_string = "Hello, World!"
   ```
2. **Single Quotes:**
   ```python
   my_string = 'Hello, World!'
   ```
3. **Triple Quotes (Multiline):**
   ```python
   my_string = '''Multiline
   String'''
   ```

## String Length

```python
length = len(my_string)
```

## Accessing Characters

- Access by index:
  ```python
  char = my_string[index]
  ```
- Access from the end (negative index):
  ```python
  char = my_string[-index]
  ```

## Slicing Strings

- Get substring from `start` to `end` (exclusive):
  ```python
  substring = my_string[start:end]
  ```
- Get substring from `start` to the end:
  ```python
  substring = my_string[start:]
  ```
- Get substring from the beginning to `end`:
  ```python
  substring = my_string[:end]
  ```
- Create a reversed copy of the string:
  ```python
  reversed_string = my_string[::-1]
  ```

## String Concatenation

```python
new_string = string1 + string2
```

## String Repetition

```python
repeated_string = my_string * n
```

## Modifying Strings

Strings in Python are immutable, so you cannot modify them directly. You can create a new modified string.

## Checking for Substrings

- Check if a substring exists in the string:
  ```python
  if substring in my_string:
  ```
- Check if the string starts with a specific prefix:
  ```python
  if my_string.startswith(prefix):
  ```
- Check if the string ends with a specific suffix:
  ```python
  if my_string.endswith(suffix):
  ```

## Changing Case

- Convert to uppercase:
  ```python
  uppercase_string = my_string.upper()
  ```
- Convert to lowercase:
  ```python
  lowercase_string = my_string.lower()
  ```
- Convert to title case:
  ```python
  titlecase_string = my_string.title()
  ```

## Stripping Whitespace

- Remove leading and trailing whitespace:
  ```python
  stripped_string = my_string.strip()
  ```
- Remove leading whitespace:
  ```python
  left_stripped = my_string.lstrip()
  ```
- Remove trailing whitespace:
  ```python
  right_stripped = my_string.rstrip()
  ```

## Splitting Strings

```python
my_list = my_string.split(separator)
```

## Joining Strings

```python
new_string = separator.join(iterable)
```

## Replacing Substrings

```python
new_string = my_string.replace(old_substring, new_substring)
```

## Formatting Strings

Use f-strings (`f"..."`) for string formatting, including variable substitution.

## String Comparison

Strings can be compared using comparison operators (`==`, `!=`, `<`, `<=`, `>`, `>=`), which compare lexicographically.
```

You can copy and paste this Markdown code into your GitHub repository or Markdown editor to create a neat cheatsheet.



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
