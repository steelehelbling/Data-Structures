class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.set_next(new_node)
            self.tail = new_node
    def remove_tail(self): 
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.tail.get_value()
            current = self.head 
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
            self.tail.set_next(None) 
            return val
    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            val = self.head.get_value()
            self.head = None
            self.tail = None
            return val
        else:
            val = self.head.get_value()
            self.head = self.head.get_next()
            return val

    def contains(self, value):
            current = self.head 
            while current:
                if current.get_value() == value:
                    return True
                current = current.get_next()
            

            
