from typing import Any, List

from linked_list_values import linked_list_values
from node import Node


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
