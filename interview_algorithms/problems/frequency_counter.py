"""Pattern: frequency counter.

This pattern is useful when the number of times each value occurs matters.
Replacing repeated searches with one or two dictionaries often reduces O(n²)
to O(n).
"""

from collections import Counter


def same_squared_naive(first: list[int], second: list[int]) -> bool:
    """Return whether ``second`` contains the squares of ``first``.

    Frequencies must match. This version copies the second list and searches it
    for each square: O(n²) time and O(n) space.
    """
    if len(first) != len(second):
        return False

    remaining = second.copy()
    for value in first:
        squared = value**2
        if squared not in remaining:
            return False
        remaining.remove(squared)
    return True


def same_squared(first: list[int], second: list[int]) -> bool:
    """Solve the same problem with counters: O(n) time and O(n) space."""
    if len(first) != len(second):
        return False

    squared_frequencies = Counter(value**2 for value in first)
    return squared_frequencies == Counter(second)


def valid_anagram(first: str, second: str) -> bool:
    """Return whether two strings contain exactly the same characters.

    The comparison is case-sensitive and includes spaces and punctuation.
    Complexity: O(n) time and O(k) space, where k is the number of distinct
    characters.
    """
    if len(first) != len(second):
        return False

    frequencies: dict[str, int] = {}
    for character in first:
        frequencies[character] = frequencies.get(character, 0) + 1

    for character in second:
        if frequencies.get(character, 0) == 0:
            return False
        frequencies[character] -= 1
    return True


if __name__ == "__main__":
    assert same_squared([1, 2, 3], [4, 1, 10])
    assert not same_squared([1, 2, 1], [4, 4, 1])
    assert valid_anagram("anagram", "nagaram")
    print("Frequency counter examples: OK")
