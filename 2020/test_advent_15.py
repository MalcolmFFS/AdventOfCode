#!/usr/bin/env python3


import unittest
from advent_15 import part_one


class TestAdvent15(unittest.TestCase):
    def test_part_one(self):
        self.assertEqual(part_one([0, 3, 6]), 436)
        self.assertEqual(part_one([1, 3, 2]), 1)
        self.assertEqual(part_one([2, 1, 3]), 10)
        self.assertEqual(part_one([1, 2, 3]), 27)
        self.assertEqual(part_one([2, 3, 1]), 78)
        self.assertEqual(part_one([3, 2, 1]), 438)
        self.assertEqual(part_one([3, 1, 2]), 1836)


if __name__ == "__main__":
    unittest.main()
