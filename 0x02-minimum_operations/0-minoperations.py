#!/usr/bin/python3
""" calculate the fewer number of
operation.
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n H characters in the file.
    """
    if n <= 1:
        return 0

    # Initialize the number of operations
    operations = 0

    # Initialize the divisor
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n = n // divisor
        divisor += 1

    return operations
