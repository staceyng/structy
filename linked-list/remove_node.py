from linked_list_values import linked_list_values
from node import Node


def remove_node(head, target_val):
    # traverse list to find target val, check if next.next exists and then update
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
