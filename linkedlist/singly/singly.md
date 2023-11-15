# Linked List Documentation

## Node Class

### `Node(data)`

- Initializes a new Node with the given data.
- Parameters:
  - `data`: The data to be stored in the node.
- Attributes:
  - `data`: The data stored in the node.
  - `next`: Reference to the next node in the linked list.

## LinkedList Class

### `LinkedList`

- Initializes an empty linked list.
- Attributes:
  - `head`: Reference to the head (first node) of the linked list.

### Methods

#### `preppend(data)`

- Adds a new node with the given data to the beginning of the linked list.
- Parameters:
  - `data`: The data to be added to the new node.

#### `append(data)`

- Adds a new node with the given data to the end of the linked list.
- Parameters:
  - `data`: The data to be added to the new node.

#### `insert_before_given(key, data)`

- Inserts a new node with the given data before the node with the specified key.
- Parameters:
  - `key`: The data of the node before which the new node is to be inserted.
  - `data`: The data to be added to the new node.
- Variables:
  - `pre_current`: The node before the current node during traversal.

#### `insert_after_given(key, data)`

- Inserts a new node with the given data after the node with the specified key.
- Parameters:
  - `key`: The data of the node after which the new node is to be inserted.
  - `data`: The data to be added to the new node.
- Variables:
  - `post_current`: The node after the current node during traversal.

#### `remove_first()`

- Removes the first node from the linked list.

#### `remove_last()`

- Removes the last node from the linked list.

#### `remove_given(key)`

- Removes the node with the specified key from the linked list.
- Parameters:
  - `key`: The data of the node to be removed.

#### `update_given(key, data)`

- Updates the node with the specified key to contain the new data.
- Parameters:
  - `key`: The data of the node to be updated.
  - `data`: The new data to be assigned to the node.
- Variables:
  - `pre_current`: The node before the current node during traversal.
  - `post_current`: The node after the current node during traversal.

#### `get_length()`

- Returns the length (number of nodes) in the linked list.

#### `move_given(key_from, key_to)`

- Moves the node with the specified key to a new position after the node with the target key.
- Parameters:
  - `key_from`: The data of the node to be moved.
  - `key_to`: The data of the node after which the moved node will be placed.
- Variables:
  - `pre_current`: The node before the current node during traversal.
  - `post_current`: The node after the current node during traversal.

#### `traverse()`

- Prints the data of all nodes in the linked list in order.

### Example Usage

```python
l = LinkedList()

# Example: Adding nodes to the linked list
l.preppend(10)
l.preppend(20)
l.append(30)
l.insert_before_given(20, 15)
l.insert_after_given(30, 35)

# Example: Removing nodes from the linked list
l.remove_first()
l.remove_last()
l.remove_given(15)

# Example: Updating nodes in the linked list
l.update_given(10, 25)

# Example: Moving a node within the linked list
l.move_given(25, 35)

# Example: Displaying the length of the linked list
print("Length:", l.get_length())

# Example: Displaying the current state of the linked list
l.traverse()