"""
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst).
The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
"""

from collections import deque


def has_path(graph, src, dst):
    # using depth first search - solve recursively
    if src == dst:
        return True

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst) is True:
            # found path
            return True

    # looked through all neighbours and paths
    return False


def has_path_breath_first(graph, src, dst):
    queue = deque([src])

    while queue:
        current = queue.popleft()
        if current == dst:
            return True

        for neighbour in graph[current]:
            queue.append(neighbour)

    return False


if __name__ == "__main__":
    graph = {"f": ["g", "i"], "g": ["h"], "h": [], "i": ["g", "k"], "j": ["i"], "k": []}

    print(has_path(graph, "f", "k"))  # True
    print(has_path_breath_first(graph, "f", "k"))
