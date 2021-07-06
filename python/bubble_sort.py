"""Custom implementation of bubble sort in python.
"""

import unittest
from typing import Any, List


def bubble_sort(arr: List[Any]) -> List[Any]:
    """Returns sorted version of arr"""
    while True:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
    return arr


class TestSort(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(bubble_sort([3, 4, 5, 2, 4, 6]), [2, 3, 4, 4, 5, 6])

    def test_case_2(self):
        self.assertEqual(bubble_sort([3, 4]), [3, 4])

    def test_case_3(self):
        self.assertEqual(bubble_sort([10, 33, -23, 34, 4]),
                         [-23, 4, 10, 33, 34])

    def test_case_4(self):
        self.assertEqual(bubble_sort([3, 0, 4, 1]), [0, 1, 3, 4])


if __name__ == '__main__':
    unittest.main()