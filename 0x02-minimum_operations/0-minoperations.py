#!/usr/bin/python3
"""Module which contains minoperations function"""

def minOperations(n):
    """
    Calculates the minimum number of operations to reach n characters.
    """
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1
    
    return operations
