"""
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments.
Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B.
Return the minimum number of semesters required to complete all n courses.
There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.
"""


def semesters_required(num_courses, prereqs):
    graph = _convert_to_adjacency_list(num_courses, prereqs)
    distance = {}
    for course in range(num_courses):
        if len(graph[course]) == 0:
            distance[course] = 1

    for course in range(num_courses):
        traverse_distance(graph, course, distance)

    return max(distance.values())


def traverse_distance(graph, node, distance):
    if node in distance:
        return distance[node]

    max_distance = 0
    for neighbor in graph[node]:
        neighbor_distance = traverse_distance(graph, neighbor, distance)
        if neighbor_distance > max_distance:
            max_distance = neighbor_distance

    distance[node] = 1 + max_distance
    return distance[node]


def _convert_to_adjacency_list(num_courses, prereqs) -> dict:
    graph = {}

    for course in range(num_courses):
        graph[course] = []

    for prereq in prereqs:
        a, b = prereq
        graph[a].append(b)

    return graph


if __name__ == "__main__":
    num_courses = 6
    prereqs = [
        (1, 2),
        (2, 4),
        (3, 5),
        (0, 5),
    ]

    # eg. 1->2->4, 0->5<-3
    # ans: 3, because sem1 - 1, 3, 0, sem2 - 2, 5, sem3 -> 4
    res = semesters_required(num_courses, prereqs)  # -> 3
    print(res)
