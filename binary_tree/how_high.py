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
