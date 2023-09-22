
## Tuples:

1. **Creating Tuples:**
   - `my_tuple = (item1, item2, ...)` - Create a tuple.

2. **Accessing Elements:**
   - `element = my_tuple[index]` - Access an element by index.

3. **Tuple Unpacking:**
   - `item1, item2 = my_tuple` - Assign tuple elements to variables.

4. **Concatenating Tuples:**
   - `new_tuple = tuple1 + tuple2` - Combine two tuples.

5. **Tuple Length:**
   - `length = len(my_tuple)` - Get the length of a tuple.

6. **Checking for an Element:**
   - `if item in my_tuple:` - Check if an item exists in the tuple.

7. **Counting Occurrences:**
   - `count = my_tuple.count(item)` - Count occurrences of an item.

8. **Finding Index:**
   - `index = my_tuple.index(item)` - Find the index of the first occurrence of an item.

9. **Immutable:**
   - Tuples are immutable, so you cannot modify elements once assigned.

# Sets:

1. **Creating Sets:**
   - `my_set = {item1, item2, ...}` - Create a set.

2. **Adding Elements:**
   - `my_set.add(item)` - Add an item to the set.

3. **Removing Elements:**
   - `my_set.remove(item)` - Remove an item from the set. Raises an error if the item is not present.
   - `my_set.discard(item)` - Remove an item from the set if it exists, without raising an error.
   - `my_set.pop()` - Remove and return an arbitrary element from the set.

4. **Set Operations:**
   - `union_set = set1.union(set2)` - Union of two sets.
   - `intersection_set = set1.intersection(set2)` - Intersection of two sets.
   - `difference_set = set1.difference(set2)` - Difference between two sets.
   - `symmetric_difference_set = set1.symmetric_difference(set2)` - Symmetric difference between two sets.

5. **Checking for an Element:**
   - `if item in my_set:` - Check if an item exists in the set.

6. **Set Length:**
   - `length = len(my_set)` - Get the number of elements in the set.

7. **Clearing a Set:**
   - `my_set.clear()` - Remove all elements from the set.

8. **Copying a Set:**
   - `new_set = my_set.copy()` - Create a shallow copy of the set.

9. **Converting to a Set:**
   - `my_set = set(my_list)` - Convert a list to a set (removes duplicates).
   - `my_set = set(my_tuple)` - Convert a tuple to a set.

## Examples

**Tuples:**

1. **Creating Tuples and Accessing Elements:**

```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Accessing the first element
print(my_tuple[3])  # Accessing the fourth element
```

**Output:**
```
1
4
```

2. **Tuple Unpacking:**

```python
point = (3, 7)
x, y = point
print("x =", x)
print("y =", y)
```

**Output:**
```
x = 3
y = 7
```

3. **Concatenating Tuples:**

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple)
```

**Output:**
```
(1, 2, 3, 4, 5, 6)
```

4. **Checking for an Element:**

```python
fruits = ("apple", "banana", "cherry")
if "banana" in fruits:
    print("Banana is in the tuple.")
```

**Output:**
```
Banana is in the tuple.
```

5. **Counting Occurrences and Finding Index:**

```python
numbers = (1, 2, 3, 2, 4, 2)
count = numbers.count(2)
index = numbers.index(4)
print("Count of 2:", count)
print("Index of 4:", index)
```

**Output:**
```
Count of 2: 3
Index of 4: 4
```

**Sets:**

1. **Creating Sets and Adding Elements:**

```python
my_set = {1, 2, 3}
my_set.add(4)
my_set.add(2)  # Adding a duplicate (no effect)
print(my_set)
```

**Output:**
```
{1, 2, 3, 4}
```

2. **Removing Elements:**

```python
my_set.remove(3)
my_set.discard(5)  # Trying to remove a non-existent element
print(my_set)
```

**Output:**
```
{1, 2, 4}
```

3. **Set Operations:**

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
symmetric_difference_set = set1.symmetric_difference(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
```

**Output:**
```
Union: {1, 2, 3, 4, 5, 6}
Intersection: {3, 4}
Difference: {1, 2}
Symmetric Difference: {1, 2, 5, 6}
```

4. **Checking for an Element:**

```python
colors = {"red", "blue", "green"}
if "blue" in colors:
    print("Blue is in the set.")
```

**Output:**
```
Blue is in the set.
```

5. **Set Length:**

```python
my_set = {10, 20, 30, 40, 50}
length = len(my_set)
print("Length:", length)
```

**Output:**
```
Length: 5
```
