"""Compute power using recursing only. No loop.
"""

import unittest

def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * power(a, n-1)


class TestPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(power(3,5), 243, "power(3,5) is 243")
        self.assertEqual(power(2,0), 1, "power(2,0) is 1")
        self.assertEqual(power(0,0), 1, "power(0,0) is 1")
        self.assertEqual(power(0,2), 0, "power(0,2) is 0")

if __name__ == "__main__":
    unittest.main()
