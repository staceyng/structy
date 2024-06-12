from typing import Any, Optional
from node import Node

def get_node_value(head, index) -> Optional[Any]:
    """
    Write a function, get_node_value, that takes in the head of a linked list and an index.
    The function should return the value of the linked list at the specified index.

    If there is no node at the given index, then return None.
    """
    index_val = None
    current = head
    pos = 0

    while current is not None:
        if pos == index:
            index_val = current.val
            break

        current = current.next
        pos += 1

    return index_val

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(get_node_value(a, 2)) # c
