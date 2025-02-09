"""
Write a function, minimum_island, that takes in a grid containing Ws and Ls
W represents water and L represents land.
The function should return the size of the smallest island.
An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island.
"""

from typing import List


def island_count(grid: List[List[str]]) -> int:
    visited = set()
    smallest = float("inf")

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore(grid, row, col, visited)
            if size > 0 and size < smallest:
                smallest = size

    return smallest


def explore(grid, row, col, visited) -> int:
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return 0

    # We dont care about water, only want to find land
    if grid[row][col] == "W":
        return 0

    # Check if land pos has been visited
    pos = (row, col)
    if pos in visited:
        return 0
    visited.add(pos)

    # Perform depth first search to find neighbouring lands
    size = 1
    size += explore(grid, row - 1, col, visited)  # up
    size += explore(grid, row + 1, col, visited)  # down
    size += explore(grid, row, col - 1, visited)  # left
    size += explore(grid, row, col + 1, visited)  # right

    return size


if __name__ == "__main__":
    grid = [
        ["W", "L", "W", "W", "W"],
        ["W", "L", "W", "W", "W"],
        ["W", "W", "W", "L", "W"],
        ["W", "W", "L", "L", "W"],
        ["L", "W", "W", "L", "L"],
        ["L", "L", "W", "W", "W"],
    ]

res = island_count(grid)  # -> 3
print(res)
