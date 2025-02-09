"""
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph.
The function should return a boolean indicating whether or not the graph contains a cycle.
"""


def has_cycle(graph):
    visited = set()
    for start_node in graph:
        if cycle_detect(graph, start_node, set(), visited):
            return True
    return False


def cycle_detect(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False


if __name__ == "__main__":
    res1 = has_cycle(
        {
            "a": ["b"],
            "b": ["c"],
            "c": ["a"],
        }
    )  # True
    print(res1)

    res2 = has_cycle(
        {
            "q": ["r", "s"],
            "r": ["t", "u"],
            "s": [],
            "t": [],
            "u": [],
            "v": ["w"],
            "w": [],
            "x": ["w"],
        }
    )  # -> False
    print(res2)
