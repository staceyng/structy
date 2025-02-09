from node import Node, linked_list_values

"""
Write a function, zipper_lists, that takes in the head of two linked lists as arguments.
The function should zipper the two lists together into single linked list by alternating nodes.
If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes.
The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.
"""


def zipper_lists(head_1, head_2):
    tail = head_1
    curr1 = head_1.next
    curr2 = head_2
    counter = 0  # when count is even: pick from list2, odd: pick from list1

    while curr1 and curr2:
        if counter % 2 == 0:
            # even
            tail.next = curr2
            curr2 = curr2.next
        else:
            # odd
            tail.next = curr1
            curr1 = curr1.next

        # update tail, counter
        tail = tail.next
        counter += 1

    if curr1 is not None:
        tail.next = curr1
    if curr2 is not None:
        tail.next = curr2

    return head_1


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    a.next = b
    b.next = c
    # a -> b -> c

    x = Node("x")
    y = Node("y")
    z = Node("z")
    x.next = y
    y.next = z
    # x -> y -> z

    res = zipper_lists(a, x)
    print(linked_list_values(res))
