"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
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
    def remove_tail(self): 
        if self.head is None and self.tail is None:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        else:
            value = self.tail.get_value()
            current = self.head 
            while current.get_next() != self.tail:
                current = current.get_next()
            self.tail = current
            self.tail.set_next(None) 
            return value


class Stack:
    def __init__(self):
        self.len = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.len

    def push(self, value):
        self.storage.add_to_tail(value)
        self.len = self.len + 1

    def pop(self):
        if self.len == 0:
            return None
        else:
            self.len = self.len - 1
            return self.storage.remove_tail()
