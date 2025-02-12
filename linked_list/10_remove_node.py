"""
Write a function, remove_node, that takes in the head of a linked list and a target value as arguments.
The function should delete the node containing the target value from the linked list and return the head of the resulting linked list.
If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

Do this in-place.

You may assume that the input list is non-empty.

You may assume that the input list contains the target.
"""

from node import Node, linked_list_values


def remove_node(head, target_val):
    # traverse list to find target val, assign prev.next = curr.next and then update prev and curr nodes
    # a -> b -> c -> d -> e
    # None -> a -> b -> c -> d -> e
    # prev   curr
    #        prev  curr
    #              prev curr
    if head.val == target_val:
        return head.next

    prev = Node(None)
    curr = head
    prev.next = curr
    while curr is not None:
        if curr.val == target_val:
            prev.next = curr.next
            break

        prev = curr
        curr = curr.next

    return head


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    # a -> b -> c -> d -> e -> f

    res = remove_node(a, "c")
    print(linked_list_values(res))
    # a -> b -> d -> e -> f
