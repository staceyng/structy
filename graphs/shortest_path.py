from collections import deque


def shortest_path(edges, node_a, node_b):
    # use breath first search (queuex)
    graph = _build_graph(edges)
    visited = set([node_a])

    queue = deque([(node_a, 0)])

    while queue:
        node, dist = queue.popleft()

        # found target node
        if node == node_b:
            return dist

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append((neighbour, dist + 1))

    return -1


def _build_graph(edges) -> dict:
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


if __name__ == "__main__":
    edges = [["w", "x"], ["x", "y"], ["z", "y"], ["z", "v"], ["w", "v"]]
    res = shortest_path(edges, "w", "z")  # -> 2
    print(res)
