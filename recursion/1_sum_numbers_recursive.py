"""
Write a function sumNumbersRecursive that takes in an array of numbers and returns the sum of all the numbers in the array.
All elements will be integers. Solve this recursively.
"""

from typing import List


def sum_numbers_recursive(numbers: List[int]) -> int:
    # base case - len(numbers) = 0
    if len(numbers) == 0:
        return 0

    return numbers[0] + sum_numbers_recursive(numbers[1:])


if __name__ == "__main__":
    example = [5, 2, 9, 10]
    ans = sum_numbers_recursive(example)
    print(ans)
