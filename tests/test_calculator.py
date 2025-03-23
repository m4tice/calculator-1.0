"""
author: @guu8hc
"""

import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    Unit tests for the Calculator class.

    Tests include:
    - Addition
    - Subtraction
    - Multiplication
    - Division (including division by zero)
    - Power
    - Factorial
    - Prime number check
    - Root calculation
    """

    def setUp(self):
        """
        initialize the calculator
        """
        self.calc = Calculator()

    def test_add(self):
        """
        add function assertation
        """
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        """
        subtract function assertation
        """
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        """
        multiply function assertation
        """
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        """
        divide function assertation
        """
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(10, 0))

    def test_power(self):
        """
        power function assertation
        """
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_factorial(self):
        """
        factorial function assertation
        """
        self.assertEqual(self.calc.factorial(5), 120)

    def test_is_prime(self):
        """
        prime number check assertation
        """
        self.assertTrue(self.calc.is_prime(7))
        self.assertFalse(self.calc.is_prime(4))

    def test_root(self):
        """
        root function assertation
        """
        self.assertEqual(self.calc.root(27, 3), 3)

if __name__ == '__main__':
    unittest.main()
