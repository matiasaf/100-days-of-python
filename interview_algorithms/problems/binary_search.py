"""Pattern: divide and conquer through binary search."""


def linear_search(values: list[int], target: int) -> int:
    """Search from left to right: O(n) time and O(1) space."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(values: list[int], target: int) -> int:
    """Search for ``target`` in a sorted list: O(log n) time, O(1) space.

    Comparing against the middle element lets us discard the half that cannot
    contain the target. Return -1 when the value is not present.
    """
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        current = values[middle]

        if current == target:
            return middle
        if current < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


if __name__ == "__main__":
    assert binary_search([1, 2, 3, 4, 5, 6], 4) == 3
    assert binary_search([1, 2, 3, 4, 5, 6], 11) == -1
    print("Search examples: OK")
