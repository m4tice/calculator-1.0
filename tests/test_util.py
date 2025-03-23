"""
author: @guu8hc
"""

import unittest
from app.util import power, factorial, is_prime, root

class TestUtil(unittest.TestCase):

    def test_power(self):
        self.assertEqual(power(2, 3), 8)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))

    def test_root(self):
        self.assertEqual(root(27, 3), 3)

if __name__ == '__main__':
    unittest.main()
