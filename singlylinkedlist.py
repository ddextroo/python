class node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        if self.head is None:
            print("empty")
        else:
            current = self.head
            while current is not None:
                print(current.value, end="|")
                print(current.next, end=" -> ")
                current = current.next
        print()


ll = LinkedList()

ll.add_node(1)
ll.add_node(2)
ll.add_node(3)

ll.display()
