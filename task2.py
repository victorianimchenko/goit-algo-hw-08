class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def sum_tree(root):
    if root is None:
        return 0

    return (
        root.key
        + sum_tree(root.left)
        + sum_tree(root.right)
    )


root = None

values = [20, 10, 30, 5, 15, 25, 40]

for value in values:
    root = insert(root, value)

print("Sum of all values:", sum_tree(root))