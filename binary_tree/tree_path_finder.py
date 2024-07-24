from node import Node


def path_finder(root, target) -> list:
    """
    Write a function, path_finder, that takes in the root of a binary tree and a target value.
    The function should return an array representing a path to the target value.
    If the target value is not found in the tree, then return None.

    You may assume that the tree contains unique values.
    """
    # solve recursively
    # edge case
    if root is None:
        return []

    # base case
    if root.val == target:
        return [root.val]

    # recursive case
    right_list = path_finder(root.right, target)
    if right_list:
        return [root.val] + right_list

    left_list = path_finder(root.left, target)
    if left_list:
        return [root.val] + left_list


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

    res = path_finder(a, "e")  # -> [ 'a', 'b', 'e' ]
    print(res)
