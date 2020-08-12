"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
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
    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.head.get_value()
            self.head = self.head.get_next()
            return value

class Queue:
    def __init__(self):
        self.len = 0
        self.data = LinkedList()
    
    def __len__(self):
        return self.len

    def enqueue(self, value):
        self.data.add_to_tail(value)
        self.len = self.len + 1

    def dequeue(self):
        if self.len == 0:
            return None
        else: 
            self.len = self.len - 1
            return self.data.remove_head()
