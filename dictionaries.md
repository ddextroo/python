
**Dictionaries:**

1. **Creating Dictionaries:**
   - `my_dict = {}` or `my_dict = dict()` - Create an empty dictionary.
   - `my_dict = {"key1": value1, "key2": value2, ...}` - Create a dictionary with key-value pairs.

2. **Accessing Values:**
   - `value = my_dict[key]` - Access a value by its key.
   - `value = my_dict.get(key, default)` - Safely access a value with a default if the key doesn't exist.

3. **Modifying Values:**
   - `my_dict[key] = new_value` - Modify a value by its key.

4. **Adding Key-Value Pairs:**
   - `my_dict[new_key] = new_value` - Add a new key-value pair to the dictionary.

5. **Removing Key-Value Pairs:**
   - `del my_dict[key]` - Remove a key-value pair by its key. Raises an error if the key doesn't exist.
   - `my_dict.pop(key, default)` - Remove and return the value associated with the key, with a default if the key doesn't exist.
   - `my_dict.popitem()` - Remove and return an arbitrary key-value pair.
   - `my_dict.clear()` - Remove all key-value pairs from the dictionary.

6. **Checking for Key Existence:**
   - `if key in my_dict:` - Check if a key exists in the dictionary.

7. **Dictionary Length:**
   - `length = len(my_dict)` - Get the number of key-value pairs in the dictionary.

8. **Accessing Keys and Values:**
   - `keys = my_dict.keys()` - Get a view of all keys in the dictionary.
   - `values = my_dict.values()` - Get a view of all values in the dictionary.
   - `items = my_dict.items()` - Get a view of all key-value pairs in the dictionary.

9. **Iterating Through a Dictionary:**
   ```python
   for key in my_dict:
       value = my_dict[key]
   ```

10. **Copying a Dictionary:**
    - `new_dict = my_dict.copy()` - Create a shallow copy of the dictionary.

11. **Merging Dictionaries:**
    - `my_dict.update(another_dict)` - Merge another dictionary into the current dictionary. If keys exist, their values are updated.

12. **Default Values:**
    - Use `defaultdict` from the `collections` module to create dictionaries with default values for missing keys.

**Creating Dictionaries:**

```python
# Creating an empty dictionary
empty_dict = {}
print(empty_dict)  # Output: {}

# Creating a dictionary with key-value pairs
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
```

**Accessing Values:**

```python
# Accessing values by key
name = my_dict["name"]
print(name)  # Output: John

# Safely accessing values with a default
country = my_dict.get("country", "USA")
print(country)  # Output: USA
```

**Modifying Values:**

```python
# Modifying a value
my_dict["age"] = 31
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York'}
```

**Adding Key-Value Pairs:**

```python
# Adding a new key-value pair
my_dict["job"] = "Engineer"
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'city': 'New York', 'job': 'Engineer'}
```

**Removing Key-Value Pairs:**

```python
# Removing a key-value pair
del my_dict["city"]
print(my_dict)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

# Using pop() to remove and return a value with a default
country = my_dict.pop("country", "USA")
print(country)  # Output: USA
```

**Checking for Key Existence:**

```python
# Checking if a key exists
if "name" in my_dict:
    print("Name exists in the dictionary.")
```

**Dictionary Length:**

```python
# Getting the number of key-value pairs
length = len(my_dict)
print(length)  # Output: 3
```

**Accessing Keys and Values:**

```python
# Getting keys and values
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(list(keys))  # Output: ['name', 'age', 'job']
print(list(values))  # Output: ['John', 31, 'Engineer']
print(list(items))  # Output: [('name', 'John'), ('age', 31), ('job', 'Engineer')]
```

**Iterating Through a Dictionary:**

```python
# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Output:
# name: John
# age: 31
# job: Engineer
```

**Copying a Dictionary:**

```python
# Creating a shallow copy of the dictionary
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}
```

You can copy and paste this Markdown into your GitHub repository.
