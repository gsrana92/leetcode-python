"""
Write a function that takes 2 inputs n and m and outputs the number of unique paths from the top left corner to the
bottom right corner of a n*m grid

Constraint: you can move only 1 unit of step right or down at a time
"""


def grid_path(n, m):
    if n == 1 or m == 1:
        return 1
    else:
        return grid_path(n - 1, m) + grid_path(n, m - 1)

print(grid_path(3,3))
