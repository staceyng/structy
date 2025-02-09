"""
Write a function, max_path_sum, that takes in the root of a binary tree that contains number values.
The function should return the maximum sum of any root to leaf path within the tree.

You may assume that the input tree is non-empty.
"""

from node import Node


def max_sum_path(root):
    # solve using recursion
    # base case/ ending condition is when node is leaf node

    if root is None:
        return float("-inf")

    if root.left is None and root.right is None:
        return root.val

    return root.val + max(max_sum_path(root.left), max_sum_path(root.right))


if __name__ == "__main__":
    a = Node(5)
    b = Node(11)
    c = Node(54)
    d = Node(20)
    e = Node(15)
    f = Node(1)
    g = Node(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    e.left = f
    e.right = g

    #        5
    #     /    \
    #    11    54
    #  /   \
    # 20   15
    #      / \
    #     1  3

    res = max_sum_path(a)  # -> 59
    print(res)
