from collections import deque

from node import Node


def breadth_first_values(root):
    """
    Write a function, breadth_first_values, that takes in the root of a binary tree.
    The function should return a list containing all values of the tree in breadth-first order.
    """

    # breath first -> left then right, then down the tree
    # approach
    # - use queue
    values = []
    if root is None:
        return values

    queue = deque()
    queue.append(root)

    while queue:
        current = queue.popleft()
        # print(current.val)
        values.append(current.val)

        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

    return values


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")
    g = Node("g")
    h = Node("h")

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      a
    #    /   \
    #   b     c
    #  / \     \
    # d   e     f
    #    /       \
    #   g         h

    res = breadth_first_values(a)
    print(res)
    #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
