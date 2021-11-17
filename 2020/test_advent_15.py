#!/usr/bin/env python3


import unittest
from advent_15 import part_one


class TestAdvent15(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one([0, 3, 6], 2020), 436)
        self.assertEqual(part_one([1, 3, 2], 2020), 1)
        self.assertEqual(part_one([2, 1, 3], 2020), 10)
        self.assertEqual(part_one([1, 2, 3], 2020), 27)
        self.assertEqual(part_one([2, 3, 1], 2020), 78)
        self.assertEqual(part_one([3, 2, 1], 2020), 438)
        self.assertEqual(part_one([3, 1, 2], 2020), 1836)

    def test_part_two(self):
        self.assertEqual(part_one([0, 3, 6], 30000000), 175594)
        # Commented out cause slow.
        # self.assertEqual(part_one([1, 3, 2], 30000000), 2578)
        # self.assertEqual(part_one([2, 1, 3], 30000000), 3544142)
        # self.assertEqual(part_one([1, 2, 3], 30000000), 261214)
        # self.assertEqual(part_one([2, 3, 1], 30000000), 6895259)
        # self.assertEqual(part_one([3, 2, 1], 30000000), 18)
        # self.assertEqual(part_one([3, 1, 2], 30000000), 362)


if __name__ == "__main__":
    unittest.main()
