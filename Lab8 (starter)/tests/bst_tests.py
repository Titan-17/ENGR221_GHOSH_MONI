import pytest
import os, sys 

# Ensure Python can locate the binarySearchTree module in the parent directory
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from binarySearchTree import BinarySearchTree


@pytest.fixture 
# Define an empty BST for testing
def emptyTree():
    """Fixture that provides an empty BinarySearchTree instance."""
    return BinarySearchTree()

@pytest.fixture 
# Define a pre-populated BST for testing
# Tree structure:
#          5
#        /   \
#       3     8
#      /
#     1
def nonemptyTree():
    """Fixture that provides a BST with multiple nodes for general testing."""
    bst = BinarySearchTree()
    bst.insert(5, "five")
    bst.insert(8, "eight")
    bst.insert(3, "three")
    bst.insert(1, "one")
    return bst


####
# isEmpty
####

@pytest.mark.isEmpty
# Verify isEmpty() correctly identifies an empty tree
def test_bst_isempty_true(emptyTree):
    """Tree with no nodes should return True."""
    assert emptyTree.isEmpty()

@pytest.mark.isEmpty
# Verify isEmpty() correctly identifies a non-empty tree
def test_bst_isempty_false(nonemptyTree):
    """Tree with nodes should return False."""
    assert not nonemptyTree.isEmpty()


####
# getRoot
####

@pytest.mark.getRoot
# Verify getRoot() returns None for an empty tree
def test_bst_getRoot_empty(emptyTree):
    """Empty tree should have no root."""
    assert emptyTree.getRoot() is None 

@pytest.mark.getRoot
# Verify getRoot() returns the root node for a non-empty tree
def test_bst_getRoot_nonempty(nonemptyTree):
    """Root of predefined tree should have key 5."""
    assert nonemptyTree.getRoot().key == 5


####
# search
####

@pytest.mark.search
# Verify search() finds an existing key
def test_bst_search_present(nonemptyTree):
    """Searching for existing key 3 should return its node."""
    assert nonemptyTree.search(3).key == 3

@pytest.mark.search
# Verify search() returns None for an absent key
def test_bst_search_absent(nonemptyTree):
    """Searching for missing key should return None."""
    assert nonemptyTree.search(4) is None


####
# lookup
####

@pytest.mark.lookup
# Verify lookup() returns the correct value for an existing key
def test_bst_lookup_present(nonemptyTree):
    """lookup(1) should return 'one'."""
    assert nonemptyTree.lookup(1) == "one"

@pytest.mark.lookup
# Verify lookup() raises an exception for an absent key
def test_bst_lookup_absent(nonemptyTree):
    """lookup() on a missing key should raise an Exception."""
    with pytest.raises(Exception):
        nonemptyTree.lookup(4)


####
# findSuccessor
####

@pytest.mark.findSuccessor
# Verify findSuccessor() finds the minimum node in a subtree
def test_bst_findSuccessor(nonemptyTree):
    """The smallest key in this tree is 1."""
    assert nonemptyTree.findSuccessor(nonemptyTree.getRoot()).key == 1


####
# delete
####

@pytest.mark.delete
# Test deleting a leaf node (no children)
def test_bst_delete_leaf(nonemptyTree, capfd):
    """After deleting leaf node (1), it should be removed from the printed structure."""
    nonemptyTree.delete(1)
    print(nonemptyTree)
    out, _ = capfd.readouterr()
    assert out == "{(5, five), {(3, three), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# Test deleting a node with one child
def test_bst_delete_child(nonemptyTree, capfd):
    """After deleting node 3 (one child), tree should restructure correctly."""
    nonemptyTree.delete(3)
    print(nonemptyTree)
    out, _ = capfd.readouterr()
    assert out == "{(5, five), {(1, one), None, None}, {(8, eight), None, None}}\n"

@pytest.mark.delete
# Test deleting a node with two children
def test_bst_delete_children(nonemptyTree, capfd):
    """Deleting root node (5) with two children should promote correct successor."""
    nonemptyTree.delete(5)
    print(nonemptyTree)
    out, _ = capfd.readouterr()
    assert out == "{(8, eight), {(3, three), {(1, one), None, None}, None}, None}\n"

@pytest.mark.delete
# Test deleting multiple nodes to form a single-branch "stick" tree
def test_bst_delete_stick(nonemptyTree, capfd):
    """Sequential deletes should update the root and structure properly."""
    nonemptyTree.delete(5)
    nonemptyTree.delete(8)
    print(nonemptyTree)
    out, _ = capfd.readouterr()
    assert out == "{(3, three), {(1, one), None, None}, None}\n"
    

####
# traverse
####

@pytest.mark.traverse
# Verify traverse() prints nodes in ascending (in-order) order
def test_bst_traverse(nonemptyTree, capfd):
    """Traversal should print nodes in ascending key order."""
    nonemptyTree.traverse()
    out, _ = capfd.readouterr()
    assert out == "(1, one)\n(3, three)\n(5, five)\n(8, eight)\n"
