def longest_path(graph):
    distance = {}
    for node in graph:
        # check if nodes are terminal (dead end)
        if len(graph[node]) == 0:
            distance[node] = 0

    for node in graph:
        traverse_distance(graph, node, distance)

    return max(distance.values())


def traverse_distance(graph, node, distance) -> int:
    # Depth first traversal

    # check if node is visited before
    if node in distance:
        return distance[node]

    # if not visited before
    largest = 0
    for neighbor in graph[node]:
        attempt = traverse_distance(graph, neighbor, distance)
        if attempt > largest:
            largest = attempt

    # store largest in distance dictionary
    distance[node] = 1 + largest
    return distance[node]


if __name__ == "__main__":
    graph = {"a": ["c", "b"], "b": ["c"], "c": []}

    res = longest_path(graph)  # -> 2
    print(res)
