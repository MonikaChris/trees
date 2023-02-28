class BST:
    """
    Binary Search Tree class
    """
    def __init__(self, root=None):
        self.root = root

    def get_nodes(self):
        """
        Returns in order list of values in BST.
        """
        def walk(root, values):
            if not root:
                return

            walk(root.left, values)
            values.append(root.val)
            walk(root.right, values)
            return values

        return walk(self.root, [])

    def insert(self, value):
        """
        Inserts value in sorted position in BST. Returns value.
        """
        def insert_val(root, val):
            if not root:
                return Node(value)

            if value < root.val:
                root.left = insert_val(root.left, val)
            if value > root.val:
                root.right = insert_val(root.right, val)
            return root

        self.root = insert_val(self.root, value)
        return value


    def remove(self, value):
        """
        Removes node with given value if in tree. Returns value.
        """
        def get_min(root):
            while root and root.left:
                root = root.left
            return root.val

        def remove_val(root, val):
            if not root:
                return root

            if val < root.val:
                root.left = remove_val(root.left, val)

            elif val > root.val:
                root.right = remove_val(root.right, val)

            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    min_val = get_min(root.right)
                    root.val = min_val
                    root.right = remove_val(root.right, min_val)
            return root

        remove_val(self.root, value)
        return value


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
