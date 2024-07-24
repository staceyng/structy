from node import Node


def tree_min_value(root):
    # traverse using breath first or depth first search, keep track of min, update min
    # assume input tree is non empty

    stack = [root]
    minimum = float("inf")  # make it a really big number first
    while stack:
        current = stack.pop()
        minimum = min(current.val, minimum)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return minimum


if __name__ == "__main__":
    a = Node(5)
    b = Node(11)
    c = Node(3)
    d = Node(4)
    e = Node(14)
    f = Node(12)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       5
    #    /    \
    #   11     3
    #  / \      \
    # 4   14     12

    res = tree_min_value(a)  # -> 3
    print(res)
