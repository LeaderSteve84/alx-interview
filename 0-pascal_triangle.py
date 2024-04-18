#!/usr/bin/python3
"""module that Returns an empty list if n <= 0"""


def pascal_triangle(n):
    """Returns an empty list if n <= 0
       Args:
           n (integer): Number of lists
    """
    if n <= 0:
        return []  # Return an empty list for non-positive n

    triangle = []
    for i in range(n):
        row = [None] * (i + 1)  # Initialize row with i+1 elements
        row[0], row[-1] = 1, 1  # set the first  and last elements to 1

        # Fill the row except the first and last element
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle
