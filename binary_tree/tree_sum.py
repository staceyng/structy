from node import Node


def tree_sum(root):
    # traverse using depth first or breath first and sum all values
    if root is None:
        return 0

    stack = [root]
    total = 0

    while stack:
        current = stack.pop()
        print(current.val)
        total += current.val

        if current.left is not None:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return total


if __name__ == "__main__":
    a = Node(1)
    b = Node(6)
    c = Node(0)
    d = Node(3)
    e = Node(-6)
    f = Node(2)
    g = Node(2)
    h = Node(2)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f
    e.left = g
    f.right = h

    #      1
    #    /   \
    #   6     0
    #  / \     \
    # 3   -6    2
    #    /       \
    #   2         2

    res = tree_sum(a)  # -> 10 = 1 + 6 + 3 -6 + 2 + 0 + 2 + 2
    print(res)
