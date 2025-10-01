"""
Hi There! Nice to Meet you!
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from double_node import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__first_node = None
        self.__last_node = None 

    def is_empty(self):
        return self.__first_node is None

    def first(self):
        if self.is_empty():
            raise Exception("List is Empty, Check again")
        return self.__first_node.get_value()
    
    def get_first_node(self):
        return self.__first_node

    def get_last_node(self):
        return self.__last_node
    
    def set_first_node(self, node):
        if node is not None and type(node) is not DoubleNode:
            raise Exception("Error: Invalid Input")
        self.__first_node = node
        if self.__first_node is not None:
            self.__first_node.set_previous_node(None)

    def set_last_node(self, node):
        if node is not node and type(node) is not DoubleNode:
            raise Exception("Invald Input")
        self.__last_node = node
        if self.__last_node is not None:
            self.__last_node.set_next_node(None)

    def find(self, value):
        cur = self.__first_node
        while cur is not None:
            if cur.get_value()== value:
                return cur
            cur = cur.get_next_node()
        return None

    def insert_front(self, value):
        new_node = DoubleNode(value,next=self.__first_node,previous=None)
        if self.is_empty():
            self.__first_node = self.__last_node = new_node
        else:
            self.__first_node.set_previous_node(new_node)
        self.__first_node = new_node

    def insert_back(self, value):
        new_node = DoubleNode(value, next=None, previous=self.__last_node)
        if self.is_empty():
            self.__first_node = self.__last_node = new_node
        else:
            self.__last_node.set_next_node(new_node)
        self.__last_node = new_node

    def insert_after(self, value_to_add, after_value):
        target = self.find(after_value)
        if target is None:
            return False
        if target.is_last():
            self.insert_back(value_to_add)
            return True
        nxt = target.get_next_node()
        new_node = DoubleNode(value_to_add, next=nxt, previous=target)
        target.set_next_node(new_node)
        nxt.set_previous_node(new_node)
        return True
    
    def delete_first_node(self):
        if self.is_empty():
            raise Exception("Error: List is empty")
        val = self.__first_node.get_value()
        if self.__first_node is self.__last_node:  
            self.__first_node = self.__last_node = None
        else:
            new_first = self.__first_node.get_next_node()
            new_first.set_previous_node(None)
            self.__first_node = new_first
        return val
    
    def delete_last_node(self):
        if self.is_empty():
            raise Exception("Error: List is empty")
        val = self.__last_node.get_value()
        if self.__first_node is self.__last_node:  
            self.__first_node = self.__last_node = None
        else:
            new_last = self.__last_node.get_previous_node()
            new_last.set_next_node(None)
            self.__last_node = new_last
        return val
    
    def delete_value(self, value):
        if self.is_empty():
            raise Exception("Error: List is empty")
        node = self.find(value)
        if node is None:
            return None 
        val = node.get_value()
        if node is self.__first_node:
            return self.delete_first_node()
        if node is self.__last_node:
            return self.delete_last_node()
        prev = node.get_previous_node()
        nxt = node.get_next_node()
        prev.set_next_node(nxt)
        nxt.set_previous_node(prev)
        return val

    def forward_traverse(self):
        cur = self.__first_node
        while cur is not None:
            print(cur.get_value())
            cur = cur.get_next_node()


    def reverse_traverse(self):
        cur = self.__last_node
        while cur is not None:
            print(cur.get_value())
            cur = cur.get_previous_node()

    def __len__(self):
        count = 0
        cur = self.__first_node
        while cur is not None:
            count += 1
            cur = cur.get_next_node()
        return count
    
    def __str__(self):
        vals = []
        cur = self.__first_node
        while cur is not None:
            vals.append(str(cur.get_value()))
            cur = cur.get_next_node()
        return "[" + " <-> ".join(vals) + "]"
    
if __name__ == "__main__":
    pass