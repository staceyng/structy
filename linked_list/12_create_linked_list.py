"""
Write a function, create_linked_list, that takes in a list of values as an argument.
The function should create a linked list containing each item of the list as the values of the nodes.
The function should return the head of the linked list.
"""

from typing import Any, List

from node import Node, linked_list_values


def create_linked_list(values: List[Any]):
    if len(values) == 0:
        return None

    dummy = Node(None)
    curr = dummy
    for i in values:
        new_node = Node(i)
        curr.next = new_node
        curr = curr.next

    return dummy.next


if __name__ == "__main__":
    res = create_linked_list(["h", "e", "y"])
    # h -> e -> y
    print(linked_list_values(res))
