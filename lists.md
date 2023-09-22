
## Lists:

1. **Creating Lists:**
   - `my_list = []` or `my_list = list()` - Create an empty list.
   - `my_list = [item1, item2, ...]` - Create a list with items.

2. **Accessing Elements:**
   - `element = my_list[index]` - Access an element by index.
   - `element = my_list[-index]` - Access elements from the end of the list (negative index).

3. **Slicing Lists:**
   - `sublist = my_list[start:end]` - Get a sublist from `start` (inclusive) to `end` (exclusive).
   - `sublist = my_list[start:]` - Get a sublist from `start` to the end.
   - `sublist = my_list[:end]` - Get a sublist from the beginning to `end`.
   - `reversed_list = my_list[::-1]` - Create a reversed copy of the list.

4. **Modifying Lists:**
   - `my_list[index] = new_value` - Modify an element by index.
   - `my_list.append(item)` - Add an item to the end of the list.
   - `my_list.insert(index, item)` - Insert an item at a specific index.
   - `my_list.extend(iterable)` - Extend the list with elements from another iterable.
   - `my_list += iterable` - Shorter way to extend the list.

5. **Removing Elements:**
   - `my_list.remove(item)` - Remove the first occurrence of an item by value.
   - `my_list.pop(index)` - Remove and return an element by index. If no index is specified, the last element is removed.
   - `my_list.pop()` - Remove and return the last element.
   - `my_list.clear()` - Remove all elements from the list.

6. **Checking for Element Existence:**
   - `if item in my_list:` - Check if an item exists in the list.

7. **List Length:**
   - `length = len(my_list)` - Get the number of elements in the list.

8. **Iterating Through a List:**
   ```python
   for item in my_list:
       # Do something with item
   ```

9. **List Comprehensions:**
   - Create new lists by applying an expression to each element of an existing list.
   ```python
   new_list = [expression for item in my_list if condition]
   ```

10. **Sorting Lists:**
    - `my_list.sort()` - Sort the list in ascending order.
    - `my_list.sort(reverse=True)` - Sort the list in descending order.
    - `sorted_list = sorted(my_list)` - Create a sorted copy of the list.

11. **Reversing Lists:**
    - `my_list.reverse()` - Reverse the elements in the list in-place.
    - `reversed_list = list(reversed(my_list))` - Create a reversed copy of the list.

12. **Copying Lists:**
    - `new_list = my_list.copy()` - Create a shallow copy of the list.

1. **Creating Lists:**

```python
# Creating an empty list
my_empty_list = []
print(my_empty_list)  # Output: []

# Creating a list with items
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

2. **Accessing Elements:**

```python
# Accessing elements by index
element = my_list[2]
print(element)  # Output: 3

# Accessing elements from the end using negative index
element = my_list[-1]
print(element)  # Output: 5
```

3. **Slicing Lists:**

```python
# Slicing a list
sublist = my_list[1:4]
print(sublist)  # Output: [2, 3, 4]

# Slicing from the beginning and end
sublist = my_list[:3]  # Equivalent to my_list[0:3]
print(sublist)  # Output: [1, 2, 3]

# Creating a reversed copy
reversed_list = my_list[::-1]
print(reversed_list)  # Output: [5, 4, 3, 2, 1]
```

4. **Modifying Lists:**

```python
# Modifying elements by index
my_list[2] = 6
print(my_list)  # Output: [1, 2, 6, 4, 5]

# Adding an item to the end
my_list.append(7)
print(my_list)  # Output: [1, 2, 6, 4, 5, 7]

# Inserting an item at a specific index
my_list.insert(2, 3)
print(my_list)  # Output: [1, 2, 3, 6, 4, 5, 7]

# Extending the list with another iterable
my_list.extend([8, 9])
print(my_list)  # Output: [1, 2, 3, 6, 4, 5, 7, 8, 9]
```

5. **Removing Elements:**

```python
# Removing an item by value
my_list.remove(3)
print(my_list)  # Output: [1, 2, 6, 4, 5, 7, 8, 9]

# Removing and returning an element by index
popped_element = my_list.pop(3)
print(popped_element)  # Output: 4
print(my_list)         # Output: [1, 2, 6, 5, 7, 8, 9]

# Removing and returning the last element
last_element = my_list.pop()
print(last_element)  # Output: 9
print(my_list)       # Output: [1, 2, 6, 5, 7, 8]

# Clearing all elements from the list
my_list.clear()
print(my_list)  # Output: []
```
