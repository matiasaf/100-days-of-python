"""Pattern: two pointers over sorted data.

The ordering lets us discard candidates without examining them one by one.
Before using this pattern, confirm that the input is actually sorted.
"""


def sum_zero_naive(values: list[int]) -> tuple[int, int] | None:
    """Return the first pair that sums to zero in O(n²) time and O(1) space."""
    for left_index, left_value in enumerate(values):
        for right_index in range(left_index + 1, len(values)):
            right_value = values[right_index]
            if left_value + right_value == 0:
                return left_value, right_value
    return None


def sum_zero(values: list[int]) -> tuple[int, int] | None:
    """Return a pair that sums to zero in a sorted list.

    If the sum is positive, no value to the right can improve it, so move the
    right pointer. If it is negative, move the left pointer.
    Complexity: O(n) time and O(1) space.
    """
    left = 0
    right = len(values) - 1

    while left < right:
        current_sum = values[left] + values[right]
        if current_sum == 0:
            return values[left], values[right]
        if current_sum > 0:
            right -= 1
        else:
            left += 1
    return None


def count_unique_values(values: list[int]) -> int:
    """Count distinct values in a sorted list: O(n) time and O(1) space."""
    if not values:
        return 0

    unique_count = 1
    previous = values[0]
    for index in range(1, len(values)):
        current = values[index]
        if current != previous:
            unique_count += 1
            previous = current
    return unique_count


if __name__ == "__main__":
    assert sum_zero([-3, -2, -1, 0, 1, 2, 3]) == (-3, 3)
    assert sum_zero([-2, 0, 1, 3]) is None
    assert count_unique_values([-2, -1, -1, 0, 1]) == 4
    print("Two-pointer examples: OK")
