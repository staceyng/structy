"""
Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.
"""

from node import Node


def leaf_list(root):
    leaves = []
    _leaf_list(root, leaves)
    return leaves


def _leaf_list(root, leaves: list):
    # null case
    if root is None:
        return []

    # use depth first search, solve recursively
    # base case
    if root.left is None and root.right is None:
        leaves.append(root.val)

    _leaf_list(root.left, leaves)
    _leaf_list(root.right, leaves)


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f

    res = leaf_list(a)  # -> [ 'd', 'e', 'f' ]
    print(res)
