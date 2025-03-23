"""
author: @guu8hc
util functions
"""

def power(a, b):
    """
    power of a to b
    """
    return a ** b

def factorial(a):
    """
    factorial of a
    """
    if a == 0:
        return 1
    return a * factorial(a - 1)

def is_prime(a):
    """
    check if a is prime
    """
    if a <= 1:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def root(a, b):
    """
    root of a to b
    """
    return a ** (1 / b)
