"""
Hey, We meet again!
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from doubly_linked_list import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()

    def is_empty(self):
        return self.__values.is_empty()
    
    def __len__(self):
        return len(self.__values)
    
    def __str__(self):
        return str(self.__values)

    def peek_left(self):
        return self.__values.first()

    def peek_right(self):
        if self.__values.is_empty():
            raise Exception("Error: List is empty")
        return self.__values.get_last_node().get_value()

    def insert_left(self, value):
        self.__values.insert_front(value)
        
    def insert_right(self, value): 
        self.__values.insert_back(value)

    def remove_left(self): 
        return self.__values.delete_first_node()

    def remove_right(self):
        return self.__values.delete_last_node()
    
if __name__ == "__main__":
    pass
