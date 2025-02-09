"""
Write a function, pair_sum, that takes in a list and a target sum as arguments.
The function should return a tuple containing a pair of indices whose elements sum to the given target.
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.
"""

from typing import List, Tuple


def pair_sum(numbers: List[int], target_sum: int) -> Tuple[int, int]:
    # Approach: Loop through nums
    # - find complement of target_sum with current value
    # - use dict to keep track of previous object and index (key = num value, val = idx)
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    i, j = 0, 0
    num_dict = {}
    for i, v in enumerate(numbers):
        pair = target_sum - v
        if pair not in num_dict:
            num_dict[v] = i
        else:
            # found pair
            j = i
            i = num_dict[pair]
            break

    return i, j


if __name__ == "__main__":
    example_numbers = [3, 2, 5, 4, 1]
    example_target_sum = 8
    ans = pair_sum(example_numbers, example_target_sum)
    print(ans)  # (0, 2)
