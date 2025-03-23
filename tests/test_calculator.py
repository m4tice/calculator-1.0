"""
author: @guu8hc
"""

import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertIsNone(self.calc.divide(10, 0))

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)

    def test_is_prime(self):
        self.assertTrue(self.calc.is_prime(7))
        self.assertFalse(self.calc.is_prime(4))

    def test_root(self):
        self.assertEqual(self.calc.root(27, 3), 3)

if __name__ == '__main__':
    unittest.main()