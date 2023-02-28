class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def contains_weight1(self, n):

        def walk(node, count, flag, n):
            if not node:
                if count == n:
                    flag = True
                count = 0
                return flag

            count += node.val
            flag = walk(node.left, count, flag, n)
            flag = walk(node.right, count, flag, n)

            return flag

        return walk(self.root, 0, False, n)


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    node5 = Node(5)
    node6 = Node(6)
    node10 = Node(10)
    node3 = Node(3)
    node4 = Node(4)
    node30 = Node(30)
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

    print(tree.contains_weight1(86))












