from node import Node

def sum_list(head) -> int:
    """
    Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument.
    The function should return the total sum of all values in the linked list.
    """
    sum = 0
    current = head

    while current is not None:
        sum += current.val
        current = current.next

    return sum

if __name__ == "__main__":
    x = Node(38)
    y = Node(4)
    x.next = y

    z = Node(100)

    print(sum_list(x)) # 42
    print(sum_list(z)) # 100
