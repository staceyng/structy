from node import Node


def tree_includes(root, target):
    # traverse tree using breath first / depth first, if target val is present break and return true
    # depth first - stack

    if root is None:
        return False

    stack = [root]
    while stack:
        current = stack.pop()
        if current.val == target:
            return True

        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)

    return False


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
    res = tree_includes(a, "a")  # -> True
    print(res)
