"""Given an array of integers, swap the min element with the max element.
"""

from typing import List
import unittest


def swap_min_max(arr: List[int]) -> List[int]:
    sorted_arr = sorted(arr)
    max = sorted_arr[-1]
    min = sorted_arr[0]

    index_max = arr.index(max)
    index_min = arr.index(min)

    # Swap the the position of min and the max element
    arr[index_max] = min
    arr[index_min] = max
    return arr


class TestPower(unittest.TestCase):
    def test_swap_min_max(self):
        self.assertEqual(swap_min_max([2,4,3,0,2]), [2,0,3,4,2])
        self.assertEqual(swap_min_max([3,0,2]), [0,3,2])
       
if __name__ == "__main__":
    unittest.main()
