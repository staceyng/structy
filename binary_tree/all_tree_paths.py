from node import Node


def all_tree_paths(root):
    paths = _all_tree_paths(root)
    for path in paths:
        path.reverse()  # this does the reverse in place
    return paths


def _all_tree_paths(root):
    # use depth first search - solve recursively

    # null case
    if root is None:
        return []

    # base case
    if root.left is None and root.right is None:
        return [[root.val]]

    all_paths = []
    # recursive case
    left_paths = _all_tree_paths(root.left)
    for path in left_paths:
        path.append(
            root.val
        )  # is appending to the back, we can use .insert but it'll be an O(n) operation
        all_paths.append(path)

    right_paths = _all_tree_paths(root.right)
    for path in right_paths:
        path.append(
            root.val
        )  # is appending to the back, we can use .insert but it'll be an O(n) operation
        all_paths.append(path)

    return all_paths


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

    res = all_tree_paths(a)  # ->
    # [
    #   [ 'a', 'b', 'd' ],
    #   [ 'a', 'b', 'e' ],
    #   [ 'a', 'c', 'f' ]
    # ]
    print(res)
