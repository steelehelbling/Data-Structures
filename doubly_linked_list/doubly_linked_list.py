"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    def get_value(self):#get value
        return self.value
    def get_next(self):#gets the next vaule in the node 
        return self.next
    def set_next(self, new_next):#updates the next node
        self.next = new_next
    def get_prev(self):#gets the prev vaule in the node
        return self.prev
    def set_prev(self, new_prev):#updates the prev node
        self.prev = new_prev
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length = self.length + 1
        new_node = ListNode(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            new_node.prev = new_node
            self.head = new_node

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head == None:
            return None

        self.length = self.length - 1
        remove = self.head.get_value()
        self.head = self.head.get_next()
        if self.head != None:
            self.head.set_prev(None)
        else:
            self.tail = None
        return remove
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length = self.length + 1        
        new_node = ListNode(value)
        if self.head == None and self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head == None:
            return None
        self.length = self.length - 1
        remove = self.tail.get_value()
        self.tail = self.tail.get_prev()
        if self.tail != None:
            self.tail.set_next(None)
        else:
            self.head = None
        return remove
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node == self.head:
            return
        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            self.length = self.length - 1
            prev_node = node.get_prev()
            next_node = node.get_next()
            prev_node.set_next(next_node)
            next_node.set_prev(prev_node)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        value = self.head.value
        gethead = self.head
        while gethead != None:
            if gethead.value > value:
                value = gethead.value
            gethead = gethead.next
        return value