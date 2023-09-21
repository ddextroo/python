**Cheatsheets**

**\*\*Tuples:\*\***

1\. \*\*Creating Tuples:\*\*

\- \`my_tuple = (item1, item2, ...)\` - Create a tuple.

2\. \*\*Accessing Elements:\*\*

\- \`element = my_tuple\[index\]\` - Access an element by index.

3\. \*\*Tuple Unpacking:\*\*

\- \`item1, item2 = my_tuple\` - Assign tuple elements to variables.

4\. \*\*Concatenating Tuples:\*\*

\- \`new_tuple = tuple1 + tuple2\` - Combine two tuples.

5\. \*\*Tuple Length:\*\*

\- \`length = len(my_tuple)\` - Get the length of a tuple.

6\. \*\*Checking for an Element:\*\*

\- \`if item in my_tuple:\` - Check if an item exists in the tuple.

7\. \*\*Counting Occurrences:\*\*

\- \`count = my_tuple.count(item)\` - Count occurrences of an item.

8\. \*\*Finding Index:\*\*

\- \`index = my_tuple.index(item)\` - Find the index of the first
occurrence of an item.

9\. \*\*Immutable:\*\*

\- Tuples are immutable, so you cannot modify elements once assigned.

**\*\*Sets:\*\***

1\. \*\*Creating Sets:\*\*

\- \`my_set = {item1, item2, ...}\` - Create a set.

2\. \*\*Adding Elements:\*\*

\- \`my_set.add(item)\` - Add an item to the set.

3\. \*\*Removing Elements:\*\*

\- \`my_set.remove(item)\` - Remove an item from the set. Raises an
error if the item is not present.

\- \`my_set.discard(item)\` - Remove an item from the set if it exists,
without raising an error.

\- \`my_set.pop()\` - Remove and return an arbitrary element from the
set.

4\. \*\*Set Operations:\*\*

\- \`union_set = set1.union(set2)\` - Union of two sets.

\- \`intersection_set = set1.intersection(set2)\` - Intersection of two
sets.

\- \`difference_set = set1.difference(set2)\` - Difference between two
sets.

\- \`symmetric_difference_set = set1.symmetric_difference(set2)\` -
Symmetric difference between two sets.

5\. \*\*Checking for an Element:\*\*

\- \`if item in my_set:\` - Check if an item exists in the set.

6\. \*\*Set Length:\*\*

\- \`length = len(my_set)\` - Get the number of elements in the set.

7\. \*\*Clearing a Set:\*\*

\- \`my_set.clear()\` - Remove all elements from the set.

8\. \*\*Copying a Set:\*\*

\- \`new_set = my_set.copy()\` - Create a shallow copy of the set.

9\. \*\*Converting to a Set:\*\*

\- \`my_set = set(my_list)\` - Convert a list to a set (removes
duplicates).

\- \`my_set = set(my_tuple)\` - Convert a tuple to a set.

**Examples:**

\*\*Tuples:\*\*

1.  \*\*Creating Tuples and Accessing Elements:\*\*

\`\`\`python

My_tuple = (1, 2, 3, 4, 5)

Print(my_tuple\[0\]) \# Accessing the first element

Print(my_tuple\[3\]) \# Accessing the fourth element

\`\`\`

\*\*Output:\*\*

\`\`\`

1

4

\`\`\`

2.  \*\*Tuple Unpacking:\*\*

\`\`\`python

Point = (3, 7)

X, y = point

Print("x =", x)

Print("y =", y)

\`\`\`

\*\*Output:\*\*

\`\`\`

X = 3

Y = 7

\`\`\`

3.  \*\*Concatenating Tuples:\*\*

\`\`\`python

Tuple1 = (1, 2, 3)

Tuple2 = (4, 5, 6)

New_tuple = tuple1 + tuple2

Print(new_tuple)

\`\`\`

\*\*Output:\*\*

\`\`\`

(1, 2, 3, 4, 5, 6)

\`\`\`

4.  \*\*Checking for an Element:\*\*

\`\`\`python

Fruits = ("apple", "banana", "cherry")

If "banana" in fruits:

Print("Banana is in the tuple.")

\`\`\`

\*\*Output:\*\*

\`\`\`

Banana is in the tuple.

\`\`\`

5.  \*\*Counting Occurrences and Finding Index:\*\*

\`\`\`python

Numbers = (1, 2, 3, 2, 4, 2)

Count = numbers.count(2)

Index = numbers.index(4)

Print("Count of 2:", count)

Print("Index of 4:", index)

\`\`\`

\*\*Output:\*\*

\`\`\`

Count of 2: 3

Index of 4: 4

\`\`\`

\*\*Sets:\*\*

1.  \*\*Creating Sets and Adding Elements:\*\*

\`\`\`python

My_set = {1, 2, 3}

My_set.add(4)

My_set.add(2) \# Adding a duplicate (no effect)

Print(my_set)

\`\`\`

\*\*Output:\*\*

\`\`\`

{1, 2, 3, 4}

\`\`\`

2.  \*\*Removing Elements:\*\*

\`\`\`python

My_set.remove(3)

My_set.discard(5) \# Trying to remove a non-existent element

Print(my_set)

\`\`\`

\*\*Output:\*\*

\`\`\`

{1, 2, 4}

\`\`\`

3.  \*\*Set Operations:\*\*

\`\`\`python

Set1 = {1, 2, 3, 4}

Set2 = {3, 4, 5, 6}

Union_set = set1.union(set2)

Intersection_set = set1.intersection(set2)

Difference_set = set1.difference(set2)

Symmetric_difference_set = set1.symmetric_difference(set2)

Print("Union:", union_set)

Print("Intersection:", intersection_set)

Print("Difference:", difference_set)

Print("Symmetric Difference:", symmetric_difference_set)

\`\`\`

\*\*Output:\*\*

\`\`\`

Union: {1, 2, 3, 4, 5, 6}

Intersection: {3, 4}

Difference: {1, 2}

Symmetric Difference: {1, 2, 5, 6}

\`\`\`

4.  \*\*Checking for an Element:\*\*

\`\`\`python

Colors = {"red", "blue", "green"}

If "blue" in colors:

Print("Blue is in the set.")

\`\`\`

\*\*Output:\*\*

\`\`\`

Blue is in the set.

\`\`\`

5.  \*\*Set Length:\*\*

\`\`\`python

My_set = {10, 20, 30, 40, 50}

Length = len(my_set)

Print("Length:", length)

\`\`\`

\*\*Output:\*\*

\`\`\`

Length: 5

\`\`\`

**\*\*Dictionaries:\*\***

1\. \*\*Creating Dictionaries:\*\*

\- \`my_dict = {}\` or \`my_dict = dict()\` - Create an empty
dictionary.

\- \`my_dict = {"key1": value1, "key2": value2, ...}\` - Create a
dictionary with key-value pairs.

2\. \*\*Accessing Values:\*\*

\- \`value = my_dict\[key\]\` - Access a value by its key.

\- \`value = my_dict.get(key, default)\` - Safely access a value with a
default if the key doesn't exist.

3\. \*\*Modifying Values:\*\*

\- \`my_dict\[key\] = new_value\` - Modify a value by its key.

4\. \*\*Adding Key-Value Pairs:\*\*

\- \`my_dict\[new_key\] = new_value\` - Add a new key-value pair to the
dictionary.

5\. \*\*Removing Key-Value Pairs:\*\*

\- \`del my_dict\[key\]\` - Remove a key-value pair by its key. Raises
an error if the key doesn't exist.

\- \`my_dict.pop(key, default)\` - Remove and return the value
associated with the key, with a default if the key doesn't exist.

\- \`my_dict.popitem()\` - Remove and return an arbitrary key-value
pair.

\- \`my_dict.clear()\` - Remove all key-value pairs from the dictionary.

6\. \*\*Checking for Key Existence:\*\*

\- \`if key in my_dict:\` - Check if a key exists in the dictionary.

7\. \*\*Dictionary Length:\*\*

\- \`length = len(my_dict)\` - Get the number of key-value pairs in the
dictionary.

8\. \*\*Accessing Keys and Values:\*\*

\- \`keys = my_dict.keys()\` - Get a view of all keys in the dictionary.

\- \`values = my_dict.values()\` - Get a view of all values in the
dictionary.

\- \`items = my_dict.items()\` - Get a view of all key-value pairs in
the dictionary.

9\. \*\*Iterating Through a Dictionary:\*\*

\`\`\`python

For key in my_dict:

Value = my_dict\[key\]

\`\`\`

10\. \*\*Copying a Dictionary:\*\*

\- \`new_dict = my_dict.copy()\` - Create a shallow copy of the
dictionary.

11\. \*\*Merging Dictionaries:\*\*

\- \`my_dict.update(another_dict)\` - Merge another dictionary into the
current dictionary. If keys exist, their values are updated.

12\. \*\*Default Values:\*\*

\- Use \`defaultdict\` from the \`collections\` module to create
dictionaries with default values for missing keys.

**Example:**

\*\*Creating Dictionaries:\*\*

\`\`\`python

\# Creating an empty dictionary

Empty_dict = {}

Print(empty_dict) \# Output: {}

\# Creating a dictionary with key-value pairs

My_dict = {"name": "John", "age": 30, "city": "New York"}

Print(my_dict) \# Output: {'name': 'John', 'age': 30, 'city': 'New
York'}

\`\`\`

\*\*Accessing Values:\*\*

\`\`\`python

\# Accessing values by key

Name = my_dict\["name"\]

Print(name) \# Output: John

\# Safely accessing values with a default

Country = my_dict.get("country", "USA")

Print(country) \# Output: USA

\`\`\`

\*\*Modifying Values:\*\*

\`\`\`python

\# Modifying a value

My_dict\["age"\] = 31

Print(my_dict) \# Output: {'name': 'John', 'age': 31, 'city': 'New
York'}

\`\`\`

\*\*Adding Key-Value Pairs:\*\*

\`\`\`python

\# Adding a new key-value pair

My_dict\["job"\] = "Engineer"

Print(my_dict) \# Output: {'name': 'John', 'age': 31, 'city': 'New
York', 'job': 'Engineer'}

\`\`\`

\*\*Removing Key-Value Pairs:\*\*

\`\`\`python

\# Removing a key-value pair

Del my_dict\["city"\]

Print(my_dict) \# Output: {'name': 'John', 'age': 31, 'job': 'Engineer'}

\# Using pop() to remove and return a value with a default

Country = my_dict.pop("country", "USA")

Print(country) \# Output: USA

\`\`\`

\*\*Checking for Key Existence:\*\*

\`\`\`python

\# Checking if a key exists

If "name" in my_dict:

Print("Name exists in the dictionary.")

\`\`\`

\*\*Dictionary Length:\*\*

\`\`\`python

\# Getting the number of key-value pairs

Length = len(my_dict)

Print(length) \# Output: 3

\`\`\`

\*\*Accessing Keys and Values:\*\*

\`\`\`python

\# Getting keys and values

Keys = my_dict.keys()

Values = my_dict.values()

Items = my_dict.items()

Print(list(keys)) \# Output: \['name', 'age', 'job'\]

Print(list(values)) \# Output: \['John', 31, 'Engineer'\]

Print(list(items)) \# Output: \[('name', 'John'), ('age', 31), ('job',
'Engineer')\]

\`\`\`

\*\*Iterating Through a Dictionary:\*\*

\`\`\`python

\# Iterating through key-value pairs

For key, value in my_dict.items():

Print(f"{key}: {value}")

\# Output:

\# name: John

\# age: 31

\# job: Engineer

\`\`\`

\*\*Copying a Dictionary:\*\*

\`\`\`python

\# Creating a shallow copy of the dictionary

New_dict = my_dict.copy()

Print(new_dict) \# Output: {'name': 'John', 'age': 31, 'job':
'Engineer'}

\`\`\`

**\*\*Lists:\*\***

1\. \*\*Creating Lists:\*\*

\- \`my_list = \[\]\` or \`my_list = list()\` - Create an empty list.

\- \`my_list = \[item1, item2, ...\]\` - Create a list with items.

2\. \*\*Accessing Elements:\*\*

\- \`element = my_list\[index\]\` - Access an element by index.

\- \`element = my_list\[-index\]\` - Access elements from the end of the
list (negative index).

3\. \*\*Slicing Lists:\*\*

\- \`sublist = my_list\[start:end\]\` - Get a sublist from \`start\`
(inclusive) to \`end\` (exclusive).

\- \`sublist = my_list\[start:\]\` - Get a sublist from \`start\` to the
end.

\- \`sublist = my_list\[:end\]\` - Get a sublist from the beginning to
\`end\`.

\- \`reversed_list = my_list\[::-1\]\` - Create a reversed copy of the
list.

4\. \*\*Modifying Lists:\*\*

\- \`my_list\[index\] = new_value\` - Modify an element by index.

\- \`my_list.append(item)\` - Add an item to the end of the list.

\- \`my_list.insert(index, item)\` - Insert an item at a specific index.

\- \`my_list.extend(iterable)\` - Extend the list with elements from
another iterable.

\- \`my_list += iterable\` - Shorter way to extend the list.

5\. \*\*Removing Elements:\*\*

\- \`my_list.remove(item)\` - Remove the first occurrence of an item by
value.

\- \`my_list.pop(index)\` - Remove and return an element by index. If no
index is specified, the last element is removed.

\- \`my_list.pop()\` - Remove and return the last element.

\- \`my_list.clear()\` - Remove all elements from the list.

6\. \*\*Checking for Element Existence:\*\*

\- \`if item in my_list:\` - Check if an item exists in the list.

7\. \*\*List Length:\*\*

\- \`length = len(my_list)\` - Get the number of elements in the list.

8\. \*\*Iterating Through a List:\*\*

\`\`\`python

For item in my_list:

\# Do something with item

\`\`\`

9\. \*\*List Comprehensions:\*\*

\- Create new lists by applying an expression to each element of an
existing list.

\`\`\`python

New_list = \[expression for item in my_list if condition\]

\`\`\`

10\. \*\*Sorting Lists:\*\*

\- \`my_list.sort()\` - Sort the list in ascending order.

\- \`my_list.sort(reverse=True)\` - Sort the list in descending order.

\- \`sorted_list = sorted(my_list)\` - Create a sorted copy of the list.

11\. \*\*Reversing Lists:\*\*

\- \`my_list.reverse()\` - Reverse the elements in the list in-place.

\- \`reversed_list = list(reversed(my_list))\` - Create a reversed copy
of the list.

12\. \*\*Copying Lists:\*\*

\- \`new_list = my_list.copy()\` - Create a shallow copy of the list.

**Examples**

1.  \*\*Creating Lists:\*\*

\`\`\`python

\# Creating an empty list

My_empty_list = \[\]

Print(my_empty_list) \# Output: \[\]

\# Creating a list with items

My_list = \[1, 2, 3, 4, 5\]

Print(my_list) \# Output: \[1, 2, 3, 4, 5\]

\`\`\`

2.  \*\*Accessing Elements:\*\*

\`\`\`python

\# Accessing elements by index

Element = my_list\[2\]

Print(element) \# Output: 3

\# Accessing elements from the end using negative index

Element = my_list\[-1\]

Print(element) \# Output: 5

\`\`\`

3.  \*\*Slicing Lists:\*\*

\`\`\`python

\# Slicing a list

Sublist = my_list\[1:4\]

Print(sublist) \# Output: \[2, 3, 4\]

\# Slicing from the beginning and end

Sublist = my_list\[:3\] \# Equivalent to my_list\[0:3\]

Print(sublist) \# Output: \[1, 2, 3\]

\# Creating a reversed copy

Reversed_list = my_list\[::-1\]

Print(reversed_list) \# Output: \[5, 4, 3, 2, 1\]

\`\`\`

4.  \*\*Modifying Lists:\*\*

\`\`\`python

\# Modifying elements by index

My_list\[2\] = 6

Print(my_list) \# Output: \[1, 2, 6, 4, 5\]

\# Adding an item to the end

My_list.append(7)

Print(my_list) \# Output: \[1, 2, 6, 4, 5, 7\]

\# Inserting an item at a specific index

My_list.insert(2, 3)

Print(my_list) \# Output: \[1, 2, 3, 6, 4, 5, 7\]

\# Extending the list with another iterable

My_list.extend(\[8, 9\])

Print(my_list) \# Output: \[1, 2, 3, 6, 4, 5, 7, 8, 9\]

\`\`\`

5.  \*\*Removing Elements:\*\*

\`\`\`python

\# Removing an item by value

My_list.remove(3)

Print(my_list) \# Output: \[1, 2, 6, 4, 5, 7, 8, 9\]

\# Removing and returning an element by index

Popped_element = my_list.pop(3)

Print(popped_element) \# Output: 4

Print(my_list) \# Output: \[1, 2, 6, 5, 7, 8, 9\]

\# Removing and returning the last element

Last_element = my_list.pop()

Print(last_element) \# Output: 9

Print(my_list) \# Output: \[1, 2, 6, 5, 7, 8\]

\# Clearing all elements from the list

My_list.clear()

Print(my_list) \# Output: \[\]

\`\`\`

**\*\*Strings:\*\***

1\. \*\*Creating Strings:\*\*

\- \`my_string = "Hello, World!"\` - Create a string with double quotes.

\- \`my_string = 'Hello, World!'\` - Create a string with single quotes.

\- \`my_string = '''Multiline

String'''\` - Create a multiline string with triple quotes.

2\. \*\*String Length:\*\*

\- \`length = len(my_string)\` - Get the length (number of characters)
of a string.

3\. \*\*Accessing Characters:\*\*

\- \`char = my_string\[index\]\` - Access a character by index.

\- \`char = my_string\[-index\]\` - Access characters from the end of
the string (negative index).

4\. \*\*Slicing Strings:\*\*

\- \`substring = my_string\[start:end\]\` - Get a substring from
\`start\` (inclusive) to \`end\` (exclusive).

\- \`substring = my_string\[start:\]\` - Get a substring from \`start\`
to the end.

\- \`substring = my_string\[:end\]\` - Get a substring from the
beginning to \`end\`.

\- \`reversed_string = my_string\[::-1\]\` - Create a reversed copy of
the string.

5\. \*\*String Concatenation:\*\*

\- \`new_string = string1 + string2\` - Concatenate two strings.

6\. \*\*String Repetition:\*\*

\- \`repeated_string = my_string \* n\` - Repeat a string \`n\` times.

7\. \*\*Modifying Strings:\*\*

\- Strings in Python are immutable, so you cannot modify them directly.
You can create a new modified string.

8\. \*\*Checking for Substrings:\*\*

\- \`if substring in my_string:\` - Check if a substring exists in the
string.

\- \`if my_string.startswith(prefix):\` - Check if the string starts
with a specific prefix.

\- \`if my_string.endswith(suffix):\` - Check if the string ends with a
specific suffix.

9\. \*\*Changing Case:\*\*

\- \`uppercase_string = my_string.upper()\` - Convert the string to
uppercase.

\- \`lowercase_string = my_string.lower()\` - Convert the string to
lowercase.

\- \`titlecase_string = my_string.title()\` - Convert the string to
title case.

10\. \*\*Stripping Whitespace:\*\*

\- \`stripped_string = my_string.strip()\` - Remove leading and trailing
whitespace.

\- \`left_stripped = my_string.lstrip()\` - Remove leading whitespace.

\- \`right_stripped = my_string.rstrip()\` - Remove trailing whitespace.

11\. \*\*Splitting Strings:\*\*

\- \`my_list = my_string.split(separator)\` - Split the string into a
list of substrings based on the separator.

12\. \*\*Joining Strings:\*\*

\- \`new_string = separator.join(iterable)\` - Join elements of an
iterable into a string using the specified separator.

13\. \*\*Replacing Substrings:\*\*

\- \`new_string = my_string.replace(old_substring, new_substring)\` -
Replace all occurrences of a substring with another substring.

14\. \*\*Formatting Strings:\*\*

\- Use f-strings (\`f"..."\`) for string formatting, including variable
substitution.

15\. \*\*String Comparison:\*\*

\- Strings can be compared using comparison operators (\`==\`, \`!=\`,
\`\<\`, \`\<=\`, \`\>\`, \`\>=\`), which compare lexicographically.

**Examples**:

\*\*1. String Length:\*\*

\`\`\`python

My_string = "Hello, World!"

Length = len(my_string)

Print(length) \# Output: 13

\`\`\`

\*\*2. Accessing Characters:\*\*

\`\`\`python

My_string = "Hello, World!"

Char = my_string\[0\]

Print(char) \# Output: "H"

\`\`\`

\*\*3. Slicing Strings:\*\*

\`\`\`python

My_string = "Hello, World!"

Substring = my_string\[0:5\]

Print(substring) \# Output: "Hello"

\`\`\`

\*\*4. String Concatenation:\*\*

\`\`\`python

String1 = "Hello, "

String2 = "World!"

New_string = string1 + string2

Print(new_string) \# Output: "Hello, World!"

\`\`\`

\*\*5. Modifying Strings (Creating a New Modified String):\*\*

\`\`\`python

My_string = "Hello, World!"

New_string = my_string.replace("World", "Python")

Print(new_string) \# Output: "Hello, Python!"

\`\`\`

\*\*6. Checking for Substrings:\*\*

\`\`\`python

Certainly! Here are some example codes and their corresponding outputs for common string operations in Python:

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

These examples cover some of the most common string operations in Python. You can use these operations to manipulate and work with strings effectively in your programs.
