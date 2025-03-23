"""
author: @guu8hc
"""

import unittest
from app.util import power, factorial, is_prime, root

class TestUtil(unittest.TestCase):
    """
    TestUtil is a test case class that contains unit tests for utility functions.
    Methods:
        test_power: Tests the power function with base 2 and exponent 3.
        test_factorial: Tests the factorial function with input 5.
        test_is_prime: Tests the is_prime function with prime number 7 and non-prime number 4.
        test_root: Tests the root function with cube root of 27.
    """
    def test_power(self):
        """
        power function assertation
        """
        self.assertEqual(power(2, 3), 8)

    def test_factorial(self):
        """
        factorial function assertation
        """
        self.assertEqual(factorial(5), 120)

    def test_is_prime(self):
        """
        prime number check assertation
        """
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))

    def test_root(self):
        """
        root function assertation
        """
        self.assertEqual(root(27, 3), 3)

if __name__ == '__main__':
    unittest.main()
