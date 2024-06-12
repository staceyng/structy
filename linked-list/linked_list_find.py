from node import Node

def linked_list_find(head, target) -> bool:
    """
    Write a function, linked_list_find, that takes in the head of a linked list and a target value.
    The function should return a boolean indicating whether or not the linked list contains the target.
    """

    # traverse linked list to store all the values in a list
    is_found = False
    current = head

    while current is not None:
        if current.val == target:
            is_found = True
            break

        current = current.next

    return is_found

if __name__ == "__main__":
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.next = b
    b.next = c
    c.next = d

    # a -> b -> c -> d

    print(linked_list_find(a, "c")) # True
