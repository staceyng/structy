from typing import Any, List
from node import Node


def linked_list_values(head) -> List[Any]:
    """
    Write a function, linked_list_values, that takes in the head of a linked list as an argument.
    The function should return a list containing all values of the nodes in the linked list.
    """
    res = []
    current = head

    while current is not None:
        res.append(current.val)
        current = current.next

    return res


if __name__ == "__main__":
    x = Node("x")
    y = Node("y")
    x.next = y

    print(linked_list_values(x))  # [ 'x', 'y' ]
    print(linked_list_values(None))  # []
