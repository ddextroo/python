

```markdown
# Python LinkedList Cheat Sheet

## LinkedList Basics

### Definition

A LinkedList is a data structure consisting of a sequence of elements, where each element points to the next element in the sequence. 

## Types of LinkedLists

1. **Singly LinkedList**: Each node has a reference to the next node.
2. **Doubly LinkedList**: Each node has references to both the next and previous nodes.
3. **Circular LinkedList**: The last node points back to the first node.

## Node Structure

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

## Creating a LinkedList

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

## LinkedList Operations

### Insertion at the Beginning

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### Insertion at the End

```python
def insert_at_end(self, data):
    new_node = Node(data)
    if not self.head:
        self.head = new_node
        return
    current = self.head
    while current.next:
        current = current.next
    current.next = new_node
```

### Deletion

```python
def delete(self, data):
    if not self.head:
        return
    if self.head.data == data:
        self.head = self.head.next
        return
    current = self.head
    while current.next:
        if current.next.data == data:
            current.next = current.next.next
            return
        current = current.next
```

### Search

```python
def search(self, data):
    current = self.head
    while current:
        if current.data == data:
            return True
        current = current.next
    return False
```

### Display

```python
def display(self):
    current = self.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
```

## Example

```python
# Creating a LinkedList
my_linkedlist = LinkedList()

# Insertion at the beginning
my_linkedlist.insert_at_beginning(3)
my_linkedlist.insert_at_beginning(2)
my_linkedlist.insert_at_beginning(1)

# Insertion at the end
my_linkedlist.insert_at_end(4)
my_linkedlist.insert_at_end(5)

# Display the LinkedList
my_linkedlist.display()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Delete an element
my_linkedlist.delete(3)

# Search for an element
found = my_linkedlist.search(4)
print(found)  # Output: True

# Display the LinkedList after deletion
my_linkedlist.display()  # Output: 1 -> 2 -> 4 -> 5 -> None
```

This cheat sheet provides an overview of Python LinkedList concepts, including types of LinkedLists, node structure, creating a LinkedList, and common LinkedList operations with code examples.
```

You can copy and paste this markdown code into a GitHub README or Markdown file.
