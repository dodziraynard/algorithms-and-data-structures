"""Custom implementation of selection sort in python.
"""

import unittest
from typing import Any, List


def selection_sort(arr: List[Any]) -> List[Any]:
    """Returns sorted version of arr"""
    for i in range(len(arr)):
        min_index = [float("inf"), float("inf")]
        for j, v in enumerate(arr[i:], i):
            if v < min_index[0]:
                min_index[0] = v
                min_index[1] = j
        temp = arr[i]
        arr[i] = min_index[0]
        arr[min_index[1]] = temp
    return arr


class TestSort(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(selection_sort([3, 4, 5, 2, 4, 6]),
                         [2, 3, 4, 4, 5, 6])

    def test_case_2(self):
        self.assertEqual(selection_sort([3, 4]), [3, 4])

    def test_case_3(self):
        self.assertEqual(selection_sort([10, 33, -23, 34, 4]),
                         [-23, 4, 10, 33, 34])


if __name__ == '__main__':
    unittest.main()