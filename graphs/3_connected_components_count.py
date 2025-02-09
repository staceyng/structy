"""
Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
The function should return the number of connected components within the graph.
"""


def connected_components_count(graph):
    count = 0
    visited = set()

    for node in graph:
        if explore(graph, node, visited):
            count += 1

    return count


def explore(graph, current, visited) -> bool:
    if current in visited:
        return False

    visited.add(current)

    for neighbour in graph[current]:
        explore(graph, neighbour, visited)

    return True


if __name__ == "__main__":
    res = connected_components_count(
        {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}
    )  # -> 2
    print(res)
