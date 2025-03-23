"""
author: @guu8hc
"""
from app.util import power, factorial, is_prime, root

class Calculator:
    """
    working as a calculator
    """
    def __init__(self):
        """
        constructor
        """
        pass

    def add(self, a, b):
        """
        add two numbers
        """
        return a + b
    
    def subtract(self, a, b):
        """
        subtract two numbers
        """
        return a - b
    
    def multiply(self, a, b):
        """
        multiply two numbers
        """
        return a * b
    
    def divide(self, a, b):
        """
        divide two numbers
        """
        return a / b if b != 0 else None
    
    def power(self, a, b):
        """
        power of a to b
        """
        return power(a, b)
    
    def factorial(self, a):
        """
        factorial of a
        """
        return factorial(a)
    
    def is_prime(self, a):
        """
        check if a is prime
        """
        return is_prime(a)
    
    def root(self, a, b):
        """
        root of a to b
        """
        return root(a, b)
