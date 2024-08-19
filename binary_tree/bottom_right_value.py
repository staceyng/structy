from node import Node
from collections import deque


def bottom_right_value(root):
    # use breath first search to solve
    # solve by using a queue, push left node into queue first, followed by right node
    q = deque([root])

    current = None
    while q: 
        current = q.popleft()
        
        if current.left is not None:
            q.append(current.left)
        
        if current.right is not None:
            q.append(current.right)
    
    return current.val





if __name__ == "__main__":
    a = Node(3)
    b = Node(11)
    c = Node(10)
    d = Node(4)
    e = Node(-2)
    f = Node(1)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = f

    res = bottom_right_value(a)  # 1
    print(res)
