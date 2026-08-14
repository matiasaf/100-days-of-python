"""Pattern: sliding window for contiguous segments."""


def max_subarray_sum_naive(values: list[int], window_size: int) -> int | None:
    """Get the maximum sum by recalculating each window: O(n*k) time."""
    _validate_window_size(window_size)
    if window_size > len(values):
        return None

    return max(
        sum(values[start : start + window_size])
        for start in range(len(values) - window_size + 1)
    )


def max_subarray_sum(values: list[int], window_size: int) -> int | None:
    """Get the maximum sum of ``window_size`` consecutive elements.

    As the window advances, subtract the outgoing element and add the incoming
    one to avoid recalculating the whole window. Complexity: O(n) time and
    O(1) space.
    """
    _validate_window_size(window_size)
    if window_size > len(values):
        return None

    current_sum = sum(values[:window_size])
    maximum_sum = current_sum

    for entering_index in range(window_size, len(values)):
        leaving_index = entering_index - window_size
        current_sum += values[entering_index] - values[leaving_index]
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum


def _validate_window_size(window_size: int) -> None:
    if window_size <= 0:
        raise ValueError("window_size must be greater than zero")


if __name__ == "__main__":
    assert max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 2) == 10
    assert max_subarray_sum([1, 2, 5, 2, 8, 1, 5], 4) == 17
    assert max_subarray_sum([], 4) is None
    print("Sliding window examples: OK")
