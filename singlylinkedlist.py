class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        
    def empty(self):
        return self.head is None
    
    def append(self,data):
        n_node = node(data)
        if self.empty():
            self.head = n_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = n_node
            
    def prepend(self,data):
        n_node = node(data)
        n_node.next = self.head
        self.head = n_node
        
    def delete(self, data):
        if self.head is None:
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
    
    def display(self):
        current = self.head
        while current:
            print(f"{current.data} -> {current.next}", end=" ")
            current = current.next
            

if __name__ == '__main__':
    ll = linkedlist()
    
    ll.append(2)
    ll.append(1)
    ll.prepend(3)
    ll.append(6)
    
    ll.display()
    
    
        