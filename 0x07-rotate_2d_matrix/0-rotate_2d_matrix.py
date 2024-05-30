#!/usr/bin/env python3
"""0x07. Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix,
    rotate it 90 degrees clockwise.
    """
    num = len(matrix)
    for i in range(num // 2):
        for j in range(i, num - i - 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[num - 1 - j][i]
            matrix[num - 1 - j][i] = matrix[num - 1 - i][num - 1 - j]
            matrix[num - 1 - i][num - 1 - j] = matrix[j][num - 1 - i]
            matrix[j][num - 1 - i] = tmp
