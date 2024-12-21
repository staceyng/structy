def largest_component(graph):
    if len(graph) == 0:
        return 0

    visited = set()
    max_length = 0

    for node in graph:
        length = explore(graph, node, visited)
        if length >= max_length:
            max_length = length

    return max_length


def explore(graph, current, visited) -> int:
    if current in visited:
        return 0

    visited.add(current)

    length = 1  # represents the node we're at right now
    for neighbour in graph[current]:
        length += explore(graph, neighbour, visited)

    return length


if __name__ == "__main__":
    res = largest_component(
        {0: [8, 1, 5], 1: [0], 5: [0, 8], 8: [0, 5], 2: [3, 4], 3: [2, 4], 4: [3, 2]}
    )  # -> 4
    print(res)
