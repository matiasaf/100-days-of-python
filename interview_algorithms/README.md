# Coding Interview Algorithms in Python

This module is separate from the 100-day course. The goal is not to memorize
solutions, but to practice a repeatable way of thinking, recognize patterns,
and learn the Python needed to express them along the way.

## The process we will use

Before writing code, follow these five steps:

1. **Understand:** restate the problem and identify its inputs, output, and
   constraints.
2. **Explore examples:** include simple, complex, empty, and invalid cases.
3. **Break it down:** describe the steps of the solution in plain language.
4. **Solve or simplify:** start with a correct solution. If you get stuck,
   isolate the difficult part and solve a simpler version.
5. **Review and refactor:** verify the result, readability, and time and space
   complexity.

During an interview, it helps to explain these steps out loud. Interviewers
evaluate more than the result: they also need to understand how you reached it.

## Current content

| Pattern | Question that helps identify it | Exercises |
|---|---|---|
| Frequency counter | Do I need to compare how often values occur? | corresponding squares, anagrams |
| Two pointers | Can sorted data help me discard values at either end? | zero sum, unique values |
| Sliding window | Am I looking for something in a contiguous segment? | maximum sum of `k` elements |
| Divide and conquer | Can I discard half of the data at each step? | binary search |

Each file contains:

- the problem statement and important decisions;
- a naive solution to use as a starting point;
- an optimized solution;
- time and space complexity;
- examples that can be run as tests.

## How to study an exercise

Take `sum_zero`, for example:

1. Read only the problem statement in `two_pointers.py`.
2. Write three cases by hand, including one with no solution.
3. Implement two nested loops first, without looking at the solution.
4. Ask yourself what can be discarded because the list is sorted.
5. Compare your idea with `sum_zero` and explain why moving each pointer is safe.
6. Run the tests and add a case that is not already covered.

## Python features used in the solutions

- `list[int]`, `tuple[int, int] | None`: type annotations.
- `dict.get(key, 0)`: reading a counter with an initial value.
- `collections.Counter`: a frequency counter from the standard library.
- `enumerate`: iterating over values together with their indexes.
- slices such as `values[:window_size]`: obtaining part of a list.
- `raise ValueError(...)`: rejecting arguments whose meaning would be ambiguous.

Type annotations help document the code, but Python does not validate them
automatically at runtime. The tests verify the behavior.

## Run everything

From the repository root:

```sh
python3 -m unittest discover -s interview_algorithms/tests -v
```

You can also open any file in `problems/` and run its examples:

```sh
python3 -m interview_algorithms.problems.two_pointers
```

## Add the next problem

Copy `problem_template.py`, rename it using `snake_case`, and complete each
section. Then add its cases to `tests/`. A good progression from here would be:

1. frequency: `same_frequency` and `are_there_duplicates`;
2. two pointers: `average_pair` and duplicate removal;
3. sliding window: longest substring without repeated characters;
4. recursion, sorting, and data structures;
5. backtracking and dynamic programming.

The goal of every addition is to explain not only **what** works, but also
**why** it works and under which constraints.
