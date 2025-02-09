"""
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B).
The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
"""


def undirected_path(edges, node_A, node_B):
    # convert edges to an adjacency list
    graph = _build_graph(edges)
    return has_path(graph, node_A, node_B, set())


def has_path(graph, src, dst, visited):
    # using depth first search - solve recursively
    if src == dst:
        return True

    # check for infinite loop
    if src in visited:
        return False

    visited.add(src)

    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst, visited) is True:
            # found path
            return True

    # looked through all neighbours and paths
    return False


def _build_graph(edges: list):
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
    edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

    res = undirected_path(edges, "j", "m")
    print(res)
