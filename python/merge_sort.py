"""Custom implementation of merge sort in python.
"""

import unittest
from typing import Any, List


def merge_sort(arr: List[Any]) -> List[Any]:
    """Returns sorted version of arr"""
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2

    sorted_left = merge_sort(arr[:mid])
    sorted_right = merge_sort(arr[mid:])

    sorted_arr = []
    while (len(sorted_left) > 0 and len(sorted_right) > 0):
        if sorted_left[0] > sorted_right[0]:
            sorted_arr.append(sorted_right[0])
            del sorted_right[0]
        else:
            sorted_arr.append(sorted_left[0])
            del sorted_left[0]

    sorted_arr += sorted_left
    sorted_arr += sorted_right

    return sorted_arr


class TestSort(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(merge_sort([3, 4, 5, 2, 4, 6]), [2, 3, 4, 4, 5, 6])

    def test_case_2(self):
        self.assertEqual(merge_sort([3, 4]), [3, 4])

    def test_case_3(self):
        self.assertEqual(merge_sort([10, 33, -23, 34, 4]),
                         [-23, 4, 10, 33, 34])

    def test_case_4(self):
        self.assertEqual(merge_sort([3, 0, 4, 1]), [0, 1, 3, 4])


if __name__ == '__main__':
    unittest.main()