"""
TODO: WRITE YOUR PROGRAM HEADER HERE
"""

class BinarySearchTree:
    """ A simple unbalanced Binary Search Tree (BST) that stores (key, value) pairs
        with unique, comparable keys and supports insert, search/lookup, delete,
        successor, traversal, and string formatting utilities. """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ Check whether the BST is empty.
            Inputs: None
            Returns: (bool) True if the tree has no nodes, False otherwise. """
        return self.__root is None
    
    def getRoot(self):
        """ Get the root node of the BST.
            Inputs: None
            Returns: (Node) The root node (or None if empty). """
        return self.__root

    def search(self, goalKey):
        """ Search for a node with the given key in the BST.
            Inputs:
                - goalKey: (any) The key to search for
            Returns: (Node or None) The node whose key == goalKey, or None. """
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        """ Recursive helper for search().
            Inputs:
                - node: (Node) root of the current subtree
                - goalKey: key being searched
            Returns: (Node or None) Node with key == goalKey, or None if absent. """
        if node is None:
            return None
        if goalKey == node.key:
            return node
        if goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        else:
            return self.__searchHelp(node.right, goalKey)

    def lookup(self, goal):
        """ Get the value associated with the given key.
            Inputs:
                - goal: (any) key whose value to return
            Returns: (any) value stored for that key
            Raises: Exception if the key is not present. """
        node = self.search(goal)
        if node is None:
            raise Exception("Key not in tree.")
        return node.value

    def findSuccessor(self, subtreeRoot):
        """ Find the in-order successor (minimum) in the given subtree.
            Inputs:
                - subtreeRoot: (Node) root of the subtree
            Returns: (Node) the node with the smallest key in that subtree. """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ Recursive helper to find the smallest node in a subtree.
            Inputs:
                - node: (Node) root of the subtree
            Returns: (Node) node with minimum key in the subtree. """
        if node is None:
            return None
        if node.left is None:
            return node
        return self.__findSuccessorHelp(node.left)
    
    def delete(self, deleteKey):
        """ Delete the node with the given key from the BST.
            Inputs:
                - deleteKey: (any) key to delete
            Returns: None
            Raises: Exception if the key is not present. """
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey)
            return
        raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ Recursive helper to delete a node by key from a subtree.
            Inputs:
                - node: (Node) root of the current subtree
                - deleteKey: (any) key to delete
            Returns: (Node) updated subtree root after deletion. """
        if node is None:
            return None
        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
            return node
        if deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
            return node
        # deleteKey == node.key: delete this node
        # Case 1: no children
        if node.left is None and node.right is None:
            return None
        # Case 2: one child
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left
        # Case 3: two children – replace with in-order successor
        succ = self.__findSuccessorHelp(node.right)
        node.key, node.value = succ.key, succ.value
        node.right = self.__deleteHelp(node.right, succ.key)
        return node

    def traverse(self) -> None:
        """ In-order traverse the BST (ascending by key) and print each node.
            Inputs: None
            Returns: None """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ Recursive in-order traversal helper.
            Inputs:
                - node: (Node) root of the current subtree
            Side effect: prints each visited node in ascending key order. """
        if node is None:
            return
        self.__traverseHelp(node.left)
        print(node)
        self.__traverseHelp(node.right)

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))
            

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    pass
