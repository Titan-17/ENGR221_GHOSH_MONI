"""
Moni Ghosh 
ENGR 221 Lab 8 
Hey! I hope your Day is going awesome!
"""

class BinarySearchTree:
    """ A simple unbalanced Binary Search Tree (BST) that stores (key, value) pairs
        with unique, comparable keys and supports insert, search/lookup, delete,
        successor, traversal, and string formatting utilities. """

    def __init__(self):
        # Expected Input: None
        # Expected Output: Initializes an empty BST with root set to None
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        # Expected Input: insertKey (any comparable type), insertValue (any type)
        # Expected Output: None (inserts a new node into the BST)
        """ Inserts the given key and value into the BST. """
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        # Expected Input: node (Node), insertKey, insertValue
        # Expected Output: Node (updated subtree root after insertion)
        """ Recursive helper method to insert a node. """
        if node == None:
            return self.__Node(insertKey, insertValue)
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        return node

    def isEmpty(self):
        # Expected Input: None
        # Expected Output: bool (True if tree is empty, else False)
        return self.__root is None
    
    def getRoot(self):
        # Expected Input: None
        # Expected Output: Node or None (root of BST)
        return self.__root

    def search(self, goalKey):
        # Expected Input: goalKey (any comparable type)
        # Expected Output: Node or None (node with matching key)
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        # Expected Input: node (Node), goalKey
        # Expected Output: Node or None
        if node is None:
            return None
        if goalKey == node.key:
            return node
        if goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        else:
            return self.__searchHelp(node.right, goalKey)

    def lookup(self, goal):
        # Expected Input: goal (key)
        # Expected Output: value associated with key OR Exception if not found
        node = self.search(goal)
        if node is None:
            raise Exception("Key not in tree.")
        return node.value

    def findSuccessor(self, subtreeRoot):
        # Expected Input: subtreeRoot (Node)
        # Expected Output: Node (smallest key in subtree)
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        # Expected Input: node (Node)
        # Expected Output: Node (minimum key node)
        if node is None:
            return None
        if node.left is None:
            return node
        return self.__findSuccessorHelp(node.left)
    
    def delete(self, deleteKey):
        # Expected Input: deleteKey (any comparable type)
        # Expected Output: None OR Exception if key not found
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey)
            return
        raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        # Expected Input: node (Node), deleteKey
        # Expected Output: Node (updated subtree root)
        if node is None:
            return None
        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
            return node
        if deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
            return node
        if node.left is None and node.right is None:
            return None
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        succ = self.__findSuccessorHelp(node.right)
        node.key, node.value = succ.key, succ.value
        node.right = self.__deleteHelp(node.right, succ.key)
        return node

    def traverse(self) -> None:
        # Expected Input: None
        # Expected Output: None (prints nodes in ascending order)
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        # Expected Input: node (Node)
        # Expected Output: None (prints nodes)
        if node is None:
            return
        self.__traverseHelp(node.left)
        print(node)
        self.__traverseHelp(node.right)

    def __str__(self) -> str:
        # Expected Input: None
        # Expected Output: str (formatted BST representation)
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        # Expected Input: return_string (str), node (Node)
        # Expected Output: str
        if node == None:
            return "None"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    class __Node:
        """ Private Node class """

        def __init__(self, key, value, left=None, right=None):
            # Expected Input: key (any), value (any), left (Node or None), right (Node or None)
            # Expected Output: Node initialized with given values
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __str__(self):
            # Expected Input: None
            # Expected Output: str ("(key, value)")
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    # Expected Input: None
    # Expected Output: No action (placeholder for testing)
    pass