#!/usr/bin/env python3
"""Min Operations"""


def minOperations(n):
    """
    Min Operations

    Args:
        n (int): number

    Returns:
        int: min operations
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
