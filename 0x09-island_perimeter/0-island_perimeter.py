#!/usr/bin/python3
""" Island Perimeter"""


def island_perimeter(grid):
    """ returns the perimeter of the island described in grid:
        Args:
            grid  (list): list of list of integers
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # check up
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                # Check down
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                # check left
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                # Check right
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1

    return perimeter
