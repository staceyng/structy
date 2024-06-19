# Class definition of a linkedList Node

from typing import Any


class Node:
    def __init__(self, val: Any):
        self.val = val
        self.next = None
