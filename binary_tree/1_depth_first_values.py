"""
Write a function, depth_first_values, that takes in the root of a binary tree.
The function should return a list containing all values of the tree in depth-first order.
"""

from node import Node


def depth_first_values(root):
    # depth first -> go deeper fisrt (traverse left side of tree when left is present)
    # approach:
    # - use stack, push right child first then left child
    # - check if stack is empty? pop stack
    # complexity:
    # - time: O(n)
    # - space: O(n)

    values = []
    stack = [root]

    while stack:
        current = stack.pop()
        print(current.val)
        values.append(current.val)

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return values


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /
    #   g

    res = depth_first_values(a)
    #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
    print(res)
