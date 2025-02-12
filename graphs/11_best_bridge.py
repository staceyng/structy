"""
Write a function, best_bridge, that takes in a grid as an argument.
The grid contains water (W) and land (L).
There are exactly two islands in the grid.
An island is a vertically or horizontally connected region of land.
Return the minimum length bridge needed to connect the two islands.

A bridge does not need to form a straight line.
"""

from collections import deque


def best_bridge(grid):
    main_island = None
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            potential_island = traverse_island(grid, r, c, set())
            if len(potential_island) > 0:
                main_island = potential_island

    visited = set(main_island)
    queue = deque([])
    for pos in main_island:
        r, c = pos
        queue.append((r, c, 0))

    while queue:
        row, col, distance = queue.popleft()
        if grid[row][col] == "L" and (row, col) not in main_island:
            return distance - 1

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # up, down, right, left
        for delta in deltas:
            delta_row, delta_col = delta
            neighbor_row = row + delta_row
            neighbor_col = col + delta_col
            neighbor_pos = (neighbor_row, neighbor_col)
            if (
                inbounds(grid, neighbor_row, neighbor_col)
                and neighbor_pos not in visited
            ):
                visited.add(neighbor_pos)
                queue.append((neighbor_row, neighbor_col, distance + 1))


def inbounds(grid, row, col):
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    return row_inbounds and col_inbounds


def traverse_island(grid, row, col, visited):
    if not inbounds(grid, row, col) or grid[row][col] == "W":
        return visited

    pos = (row, col)
    if pos in visited:
        return visited

    visited.add(pos)

    traverse_island(grid, row - 1, col, visited)
    traverse_island(grid, row + 1, col, visited)
    traverse_island(grid, row, col - 1, visited)
    traverse_island(grid, row, col + 1, visited)
    return visited
