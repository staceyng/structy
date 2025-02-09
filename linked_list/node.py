# Class definition of a linkedList Node
# contains helper functions for linkedlist data structure

from typing import Any, List


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next = None


def linked_list_values(head) -> List[Any]:
    res = []
    current = head

    while current is not None:
        res.append(current.val)
        current = current.next

    return res
