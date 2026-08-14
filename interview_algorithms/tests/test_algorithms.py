import unittest

from interview_algorithms.problems.binary_search import binary_search, linear_search
from interview_algorithms.problems.frequency_counter import (
    same_squared,
    same_squared_naive,
    valid_anagram,
)
from interview_algorithms.problems.sliding_window import (
    max_subarray_sum,
    max_subarray_sum_naive,
)
from interview_algorithms.problems.two_pointers import (
    count_unique_values,
    sum_zero,
    sum_zero_naive,
)


class FrequencyCounterTests(unittest.TestCase):
    def test_same_squared_accepts_matching_values_and_frequencies(self) -> None:
        for solution in (same_squared_naive, same_squared):
            with self.subTest(solution=solution.__name__):
                self.assertTrue(solution([1, 2, 3], [4, 1, 9]))
                self.assertFalse(solution([1, 2, 1], [4, 4, 1]))
                self.assertTrue(solution([], []))

    def test_valid_anagram(self) -> None:
        self.assertTrue(valid_anagram("anagram", "nagaram"))
        self.assertTrue(valid_anagram("", ""))
        self.assertFalse(valid_anagram("aaz", "zza"))
        self.assertFalse(valid_anagram("Python", "python"))


class TwoPointersTests(unittest.TestCase):
    def test_sum_zero(self) -> None:
        values = [-3, -2, -1, 0, 1, 2, 3]
        for solution in (sum_zero_naive, sum_zero):
            with self.subTest(solution=solution.__name__):
                self.assertEqual(solution(values), (-3, 3))
                self.assertIsNone(solution([1, 2, 3]))

    def test_count_unique_values(self) -> None:
        self.assertEqual(count_unique_values([]), 0)
        self.assertEqual(count_unique_values([1, 1, 1, 1, 2]), 2)
        self.assertEqual(count_unique_values([-2, -1, -1, 0, 1]), 4)


class SlidingWindowTests(unittest.TestCase):
    def test_max_subarray_sum(self) -> None:
        cases = [
            ([1, 2, 5, 2, 8, 1, 5], 2, 10),
            ([1, 2, 5, 2, 8, 1, 5], 4, 17),
            ([-4, -2, -8], 2, -6),
            ([], 4, None),
        ]
        for solution in (max_subarray_sum_naive, max_subarray_sum):
            for values, window_size, expected in cases:
                with self.subTest(solution=solution.__name__, values=values):
                    self.assertEqual(solution(values, window_size), expected)

    def test_window_size_must_be_positive(self) -> None:
        for solution in (max_subarray_sum_naive, max_subarray_sum):
            with self.subTest(solution=solution.__name__):
                with self.assertRaises(ValueError):
                    solution([1, 2, 3], 0)


class SearchTests(unittest.TestCase):
    def test_searches(self) -> None:
        values = [1, 2, 3, 4, 5, 6]
        for solution in (linear_search, binary_search):
            with self.subTest(solution=solution.__name__):
                self.assertEqual(solution(values, 4), 3)
                self.assertEqual(solution(values, 6), 5)
                self.assertEqual(solution(values, 11), -1)
                self.assertEqual(solution([], 1), -1)


if __name__ == "__main__":
    unittest.main()
