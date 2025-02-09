"""
Write a function, pair_product, that takes in a list and a target product as arguments.
The function should return a tuple containing a pair of indices whose elements multiply to the given target.
The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.
"""

from typing import List, Tuple


def pair_product(numbers: List[int], target_product: int) -> Tuple[int, int]:
    # Approach: Loop through nums
    # - find complement of target_product with current value
    # - use dict to keep track of previous object and index (key = num value, val = idx)
    # Time Complexity: O(n)
    # Space Complexity: O(n)

    i, j = 0, 0
    num_dict = {}
    for i, v in enumerate(numbers):
        pair = target_product / v
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
    example_target_product = 8
    ans = pair_product(example_numbers, example_target_product)
    print(ans)  # (1, 3)
