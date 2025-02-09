"""
Write a function, level_averages, that takes in the root of a binary tree that contains number values.
The function should return a list containing the average value of each level.
"""

from node import Node


def level_averages(root):
    # similar to tree levels, traverse tree recursively with breath first
    # then compute avgs

    levels = []
    _traverse_tree_by_level(root, levels, 0)

    avgs = []
    for lv in levels:
        avg = sum(lv) / len(lv)
        avgs.append(avg)

    return avgs


def _traverse_tree_by_level(root, levels, level_num):
    if root is None:
        return

    if level_num == len(levels):
        levels.append([root.val])
    else:
        levels[level_num].append(root.val)

    _traverse_tree_by_level(root.left, levels, level_num + 1)
    _traverse_tree_by_level(root.right, levels, level_num + 1)


if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    #       3
    #    /    \
    #   11     4
    #  / \      \
    # 4   -2     1

    res = level_averages(a)  # -> [ 3, 7.5, 1 ]
    print(res)
