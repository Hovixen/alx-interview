#!/usr/bin/python3
""" Island perimeter function """


def island_perimeter(grid):
    """ function returns the perimeter of an island """
    rows = len(grid)
    columns = len(grid[0])

    perimeter = 0

    for m in range(rows):
        for n in range(columns):
            # check if element is land [1]
            if grid[m][n] == 1:
                # check if up is water [0]
                if grid[m-1][n] == 0 or m == 0:
                    perimeter += 1
                # check if down is water [0]
                if grid[m+1][n] == 0 or m == rows - 1:
                    perimeter += 1
                # check if left is water [0]
                if grid[m][n-1] == 0 or n == 0:
                    perimeter += 1
                # check if right is water [0]
                if grid[m][n+1] == 0 or n == columns - 1:
                    perimeter += 1
    return perimeter
