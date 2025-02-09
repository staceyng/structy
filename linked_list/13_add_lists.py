"""
Write a function, add_lists, that takes in the head of two linked lists, each representing a number.
The nodes of the linked lists contain digits as values.
The nodes in the input lists are reversed; this means that the least significant digit of the number is the head. The function should return the head of a new linked listed representing the sum of the input lists. The output list should have its digits reversed as well.

You must do this by traversing through the linked lists once.

Say we wanted to compute 621 + 354 normally. The sum is 975:

621
+ 354
-----
975

Then, the reversed linked list format of this problem would appear as:

    1 -> 2 -> 6
 +  4 -> 5 -> 3
--------------
    5 -> 7 -> 9
"""

from node import Node, linked_list_values


def add_lists(head_1, head_2) -> int:

    carry = 0
    dummy_head = Node(None)
    tail = dummy_head
    curr1 = head_1
    curr2 = head_2

    while curr1 is not None or curr2 is not None or carry == 1:
        val1 = 0 if curr1 is None else curr1.val
        val2 = 0 if curr2 is None else curr2.val

        sum = val1 + val2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10

        tail.next = Node(digit)
        tail = tail.next

        if curr1 is not None:
            curr1 = curr1.next

        if curr2 is not None:
            curr2 = curr2.next

    return dummy_head.next


if __name__ == "__main__":
    a1 = Node(1)
    a2 = Node(2)
    a3 = Node(6)
    a1.next = a2
    a2.next = a3
    # 1 -> 2 -> 6

    b1 = Node(4)
    b2 = Node(5)
    b3 = Node(3)
    b1.next = b2
    b2.next = b3
    # 4 -> 5 -> 3

    res = add_lists(a1, b1)  # 5 -> 7 -> 9
    print(linked_list_values(res))
