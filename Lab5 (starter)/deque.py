"""
Hey there, We meet again!
Moni Ghosh 
ENGR 221
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from doubly_linked_list import DoublyLinkedList

class Deque():
    def __init__(self):
        # Initializes an empty deque using a DoublyLinkedList
        # Input: None
        # Output: None
        self.__values = DoublyLinkedList()

    def is_empty(self):
        # Checks if the deque is empty
        # Input: None
        # Output: Boolean (True if empty, False otherwise)
        return self.__values.is_empty()
    
    def __len__(self):
        # Returns the number of elements in the deque
        # Input: None
        # Output: Integer (number of elements)
        return len(self.__values)
    
    def __str__(self):
        # Returns string representation of the deque
        # Input: None
        # Output: String (e.g., "[1, 2, 3]")
        return str(self.__values)

    def peek_left(self):
        # Returns the value at the front (left) without removing it
        # Input: None
        # Output: Value at the front
        # Raises: Exception if deque is empty (depends on DoublyLinkedList implementation)
        return self.__values.first()

    def peek_right(self):
        # Returns the value at the back (right) without removing it
        # Input: None
        # Output: Value at the back
        # Raises: Exception if deque is empty
        if self.__values.is_empty():
            raise Exception("Error: List is empty")
        return self.__values.get_last_node().get_value()

    def insert_left(self, value):
        # Inserts a value at the front (left side) of the deque
        # Input: value (any data type)
        # Output: None
        self.__values.insert_front(value)
        
    def insert_right(self, value): 
        # Inserts a value at the back (right side) of the deque
        # Input: value (any data type)
        # Output: None
        self.__values.insert_back(value)

    def remove_left(self): 
        # Removes and returns the value from the front (left side)
        # Input: None
        # Output: Removed value
        # Raises: Exception if deque is empty (depends on DoublyLinkedList implementation)
        return self.__values.delete_first_node()

    def remove_right(self):
        # Removes and returns the value from the back (right side)
        # Input: None
        # Output: Removed value
        # Raises: Exception if deque is empty (depends on DoublyLinkedList implementation)
        return self.__values.delete_last_node()
    
if __name__ == "__main__":
    # No direct execution behavior defined
    # You can add test cases here if needed
    pass