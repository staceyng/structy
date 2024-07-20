from linked_list_values import linked_list_values
from node import Node


def reverse_list(head):
    prev = None
    current = head

    # None   A    B    C    D    None
    # prev curr curr.next
    # prev curr next
    # None <- A   B    C    D    None
    #       prev curr next

    while current is not None:
        next = (
            current.next
        )  # save current.next to a variable next because we might lose access to the B Node
        current.next = prev

        # move positions
        prev = current
        current = next

    return prev


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

    res = reverse_list(a)  # f -> e -> d -> c -> b -> a
    print(linked_list_values(res))
