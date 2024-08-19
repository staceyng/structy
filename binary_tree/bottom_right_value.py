from node import Node


def bottom_right_value(root):
    # solve recursively
    # base case
    if root.left is None and root.right is None:
        return root.value

    # recursive case
    if root.right:
        right = bottom_right_value(root.right)
        return right.value


if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(10)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    res = bottom_right_value(a)  # 1
    print(res)
