"""
Write a function, how_high, that takes in the root of a binary tree.
The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.
"""

from node import Node


def how_high(root):
    # solve recursively
    # base case
    if root is None:
        return -1

    # recursive case
    left_height = how_high(root.left)
    right_height = how_high(root.right)
    return 1 + max(left_height, right_height)


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

    res = how_high(a)  # 2
    print(res)
