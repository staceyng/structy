"""
Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column.
In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots.
The function should return a number representing the length of the shortest path from the starting position to a carrot.
You may move up, down, left, or right, but cannot pass through walls (X).
If there is no possible path to a carrot, then return -1.
"""

from collections import deque


def closest_carrot(grid, starting_row, starting_col):
    # use breath first search
    queue = deque([(starting_row, starting_col, 0)])
    visited = set([(starting_row, starting_col)])

    while queue:
        row, col, dist = queue.popleft()

        if grid[row][col] == "C":
            return dist

        deltas = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]  # relative positions up, down, left, right

        for d in deltas:
            dr, dc = d
            neighbour_row = row + dr
            neighbour_col = col + dc

            # check if neighbour_row and neighhour_cols are inbounds
            is_row_inbounds = neighbour_row >= 0 and neighbour_row < len(grid)
            is_col_inbounds = neighbour_col >= 0 and neighbour_col < len(grid[0])

            if (
                is_row_inbounds
                and is_col_inbounds
                and (neighbour_row, neighbour_col) not in visited
                and grid[neighbour_row][neighbour_col] != "X"
            ):
                visited.add((neighbour_row, neighbour_col))
                queue.append((neighbour_row, neighbour_col, dist + 1))

    return -1


if __name__ == "__main__":
    grid = [
        ["O", "O", "O", "O", "O"],
        ["O", "X", "O", "O", "O"],
        ["O", "X", "X", "O", "O"],
        ["O", "X", "C", "O", "O"],
        ["O", "X", "X", "O", "O"],
        ["C", "O", "O", "O", "O"],
    ]

    res = closest_carrot(grid, 1, 2)  # 4
    print(res)
