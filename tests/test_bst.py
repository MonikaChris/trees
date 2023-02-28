import pytest
from bst import BST, Node


def test_insert_leaf_val(tree1):
    tree1.insert(8)
    actual = tree1.get_nodes()
    expected = [3, 7, 8, 10, 16, 18, 22]

    assert actual == expected


def test_insert_mid_one_subtree(tree1):
    tree1.insert(6)
    actual = tree1.get_nodes()
    expected = [3, 6, 7, 10, 16, 18, 22]

    assert actual == expected


def test_insert_mid_two_subtrees(tree1):
    tree1.insert(17)
    actual = tree1.get_nodes()
    expected = [3, 7, 10, 16, 17, 18, 22]

    assert actual == expected


def test_insert_empty_tree():
    tree = BST()
    tree.insert(1)

    actual = tree.get_nodes()
    expected = [1]

    assert actual == expected


def test_remove_leaf_node(tree1):
    tree1.remove(3)
    actual = tree1.get_nodes()
    expected = [7, 10, 16, 18, 22]

    assert actual == expected


def test_remove_one_child_node(tree1):
    tree1.remove(7)
    actual = tree1.get_nodes()
    expected = [3, 10, 16, 18, 22]

    assert actual == expected


def test_remove_two_child_node(tree1):
    tree1.remove(18)
    actual = tree1.get_nodes()
    expected = [3, 7, 10, 16, 22]

    assert actual == expected


def test_remove_val_not_in_tree(tree1):
    tree1.remove(5)
    actual = tree1.get_nodes()
    expected = [3, 7, 10, 16, 18, 22]

    assert actual == expected

@pytest.fixture
def tree1():
    #       (10)
    #      /    \
    #    (7)    (18)
    #   /  \    /   \
    # (3)     (16)  (22)

    node10 = Node(10)
    node7 = Node(7)
    node3 = Node(3)
    node18 = Node(18)
    node16 = Node(16)
    node22 = Node(22)

    node10.left = node7
    node10.right = node18
    node7.left = node3
    node18.left = node16
    node18.right = node22

    tree = BST(node10)
    return tree
