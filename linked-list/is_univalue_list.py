from node import Node


def is_univalue_list(head) -> bool:
    """
    Write a function, is_univalue_list, that takes in the head of a linked list as an argument.
    The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

    You may assume that the input list is non-empty.
    """
    # traverse linked list to keep track of value, if val is different exit and return False
    val = None
    curr = head

    while curr is not None:
        if val is None:
            val = curr.val
        else:
            if curr.val != val:
                return False
        curr = curr.next

    return True


if __name__ == "__main__":
    a = Node(7)
    b = Node(7)
    c = Node(7)

    a.next = b
    b.next = c

    # 7 -> 7 -> 7
    res = is_univalue_list(a)  # True
    print(res)
