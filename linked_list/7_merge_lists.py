"""
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments.
The function should merge the two lists together into single sorted linked list.
The function should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.
"""

from node import Node, linked_list_values


def merge_lists(head_1, head_2):

    dummy_head = Node(None)
    tail = dummy_head
    curr1 = head_1
    curr2 = head_2

    while curr1 is not None and curr2 is not None:
        if curr1.val < curr2.val:
            tail.next = curr1
            curr1 = curr1.next
        else:
            tail.next = curr2
            curr2 = curr2.next

        tail = tail.next

    if curr1 is not None:
        tail.next = curr1
    if curr2 is not None:
        tail.next = curr2

    return dummy_head.next


if __name__ == "__main__":
    a = Node(5)
    b = Node(7)
    c = Node(10)
    d = Node(12)
    e = Node(20)
    f = Node(28)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f
    # 5 -> 7 -> 10 -> 12 -> 20 -> 28

    q = Node(6)
    r = Node(8)
    s = Node(9)
    t = Node(25)
    q.next = r
    r.next = s
    s.next = t
    # 6 -> 8 -> 9 -> 25

    res = merge_lists(a, q)
    print(linked_list_values(res))
    # 5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28
