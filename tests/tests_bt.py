import pytest
from bt import BinaryTree, Node


def test_true_path_15(tree1):
    assert tree1.contains_weight1(15)


def test_true_path_14(tree1):
    assert tree1.contains_weight1(14)

def test_true_path_17(tree1):
    assert tree1.contains_weight1(17)


def test_true_path_27(tree1):
    assert tree1.contains_weight1(27)

def test_true_path_85(tree1):
    assert tree1.contains_weight1(85)


def test_true_path_95(tree1):
    assert tree1.contains_weight1(95)


def test_true_path_17(tree1):
    assert tree1.contains_weight1(46)


def test_true_path_86(tree1):
    assert tree1.contains_weight1(86)


def test_false_path_10(tree1):
    assert not tree1.contains_weight1(10)


@pytest.fixture
def tree1():
    #                (5)
    #           /              \
    #         (6)               (10)
    #        /  \            /       \
    #      (3)  (4)        (30)     (11)
    #     /  \  / \        / \       / \
    #   (1) (0)(2) (12) (40) (50) (20) (60)
    #Path Sums:
    # 15, 14, 17, 27, 85, 95, 46, 86

    node5 = Node(5)
    node6 = Node(6)
    node10 = Node(10)
    node3 = Node(3)
    node4 = Node(4)
    node30= Node(30)
    node11 = Node(11)
    node1 = Node(1)
    node0 = Node(0)
    node2 = Node(2)
    node12 = Node(12)
    node40 = Node(40)
    node50 = Node(50)
    node20 = Node(20)
    node60 = Node(60)

    node5.left = node6
    node5.right = node10
    node6.left = node3
    node6.right = node4
    node10.left = node30
    node10.right = node11
    node3.left = node1
    node3.right = node0
    node4.left = node2
    node4.right = node12
    node30.left = node40
    node30.right = node50
    node11.left = node20
    node11.right = node60

    tree = BinaryTree(node5)
    return tree