"""
Write a function, insert_node, that takes in the head of a linked list, a value, and an index.
The function should insert a new node with the value into the list at the specified index.
Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.
"""

from node import Node, linked_list_values


def insert_node(head, value, index):

    curr_index = 0
    curr = head

    # a -> b -> c -> d
    # curr(0)
    #      curr(1)
    #
    #            curr(2)

    if index == 0:
        new_node = Node(value)
        new_node.next = curr
        return new_node

    while curr is not None:
        print(curr.val, curr_index)
        if curr_index == index - 1:
            # print("found index, insert new node")
            new_node = Node(value)
            following = curr.next
            curr.next = new_node
            new_node.next = following

        curr = curr.next
        curr_index += 1

    return head


if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    res = insert_node(a, "x", 2)
    # a -> b -> x -> c -> d
    print(linked_list_values(res))
