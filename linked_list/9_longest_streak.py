"""
Write a function, longest_streak, that takes in the head of a linked list as an argument.
The function should return the length of the longest consecutive streak of the same value within the list.
"""

from node import Node


def longest_streak(head) -> int:
    # traverse linked list to keep track of value, if val is different exit and return False
    val = None
    curr = head
    curr_streak = 0
    max_streak = 0

    while curr is not None:
        if val is None:
            val = curr.val
            curr_streak = 1
        else:
            if curr.val == val:
                curr_streak += 1
            else:
                val = curr.val
                curr_streak = 1
        # print(f"{curr.val=}, {curr_streak=}")
        curr = curr.next
        max_streak = max(curr_streak, max_streak)

    return max_streak


if __name__ == "__main__":
    # a = Node(9)
    # b = Node(9)
    # c = Node(1)
    # d = Node(9)
    # e = Node(9)
    # f = Node(9)

    # a.next = b
    # b.next = c
    # c.next = d
    # d.next = e
    # e.next = f

    # # 9 -> 9 -> 1 -> 9 -> 9 -> 9
    # res = longest_streak(a)  # 3
    # print(res)

    a = Node(5)
    b = Node(5)
    c = Node(7)
    d = Node(7)
    e = Node(7)
    f = Node(6)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # 5 -> 5 -> 7 -> 7 -> 7 ->  6

    res2 = print(longest_streak(a))  # 3
