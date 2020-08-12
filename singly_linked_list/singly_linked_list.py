class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 
    def get_value(self):#get value
        return self.value
    def get_next(self):#gets the next vaule in the node 
        return self.next
    def set_next(self, new_next):#updates the next node
        self.next = new_next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        new_node = Node(value)#adding a new node value
        if self.head is None and self.tail is None:#checks if empty
            self.head = new_node#adding a new node value to head
            self.tail = new_node#adding a new node value to tail
        else: 
            self.tail.set_next(new_node)#otherwize we need to update the old value to the new value
            self.tail = new_node #updates to add new end to the arry to make sure we have the right tail
    def remove_tail(self): 
        if self.head is None and self.tail is None:#return none if empty because we are deleteing the tail
            return None
        if self.head == self.tail:#checks if we have one item
            val = self.head.get_value()
            self.head = None#delete all items
            self.tail = None
            return val#return new value
        else:
            val = self.tail.get_value()
            current = self.head 
            while current.get_next() is not self.tail:#we need to search down from the head all the way down the list 
                current = current.get_next()
            else:
                self.tail = current#set new tail to new last postion
                self.tail.set_next(None) #removes last item
                return val
                
            
    def remove_head(self):
        if self.head is None and self.tail is None:
            return None
        if self.head is self.tail:
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
                if current.get_value() == value:#checks if contain = value return true
                    return True
                current = current.get_next()#goes through list
            
        
