from collections import deque

from node import Node


def tree_levels(root):
    # null case
    if root is None:
        return []

    # use breath first search
    collection = []
    queue = deque([(root, 0)])

    while queue:
        current, level_num = queue.popleft()

        if len(collection) == level_num:
            collection.append([current.val])
        else:
            collection[level_num].append(current.val)

        if current.left is not None:
            queue.append((current.left, level_num + 1))
        if current.right is not None:
            queue.append((current.right, level_num + 1))

    return collection


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

    res = tree_levels(a)  # ->
    # [
    #   ['a'],
    #   ['b', 'c'],
    #   ['d', 'e', 'f']
    # ]

    print(res)
