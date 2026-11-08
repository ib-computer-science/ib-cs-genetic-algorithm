import unittest

from random_utils import random_integer_pair, random_sorted_integer_pair, random_uniform


class RandomIntegerPairTest(unittest.TestCase):
    def test_pair_is_distinct_and_in_range(self):
        for _ in range(1000):
            a, b = random_integer_pair(10)
            self.assertNotEqual(a, b)
            self.assertTrue(0 <= a < 10)
            self.assertTrue(0 <= b < 10)

    def test_only_possible_pair_when_upper_is_two(self):
        for _ in range(100):
            a, b = random_integer_pair(2)
            self.assertEqual({a, b}, {0, 1})


class RandomSortedIntegerPairTest(unittest.TestCase):
    def test_pair_is_sorted_distinct_and_in_range(self):
        for _ in range(1000):
            a, b = random_sorted_integer_pair(10)
            self.assertLess(a, b)
            self.assertTrue(0 <= a < 10)
            self.assertTrue(0 <= b < 10)


class RandomUniformTest(unittest.TestCase):
    def test_in_unit_interval(self):
        for _ in range(1000):
            p = random_uniform()
            self.assertTrue(0.0 <= p < 1.0)


if __name__ == "__main__":
    unittest.main()
