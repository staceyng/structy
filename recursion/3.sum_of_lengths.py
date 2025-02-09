"""
Write a function sumOfLengths that takes in a list of strings and returns the total length of the strings.

You must solve this recursively.
"""

from typing import List


def sum_of_lengths(strings: List[str]) -> int:
    # base case
    if len(strings) == 0:
        return 0

    return len(strings[0]) + sum_of_lengths(strings[1:])


if __name__ == "__main__":
    example1 = []
    example2 = ["goat", "cat", "purple"]  # 13
    ans = sum_of_lengths(example2)
    print(ans)
