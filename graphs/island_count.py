from typing import List


def island_count(grid: List[List[str]]):
    visited = set()
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                count += 1

    return count


def explore(grid, row, col, visited) -> bool:
    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])

    if not row_inbounds or not col_inbounds:
        return False

    # We dont care about water, only want to find land
    if grid[row][col] == "W":
        return False

    # Check if land pos has been visited
    pos = (row, col)
    if pos in visited:
        return False
    visited.add(pos)

    # Perform depth first search to find neighbouring lands
    explore(grid, row - 1, col, visited)  # up
    explore(grid, row + 1, col, visited)  # down
    explore(grid, row, col - 1, visited)  # left
    explore(grid, row, col + 1, visited)  # right

    return True


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
