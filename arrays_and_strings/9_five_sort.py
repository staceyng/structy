"""
Write a function, five_sort, that takes in a list of numbers as an argument.
The function should rearrange elements of the list such that all 5s appear at the end.
Your function should perform this operation in-place by mutating the original list. The function should return the list.

Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.
"""

from typing import List


def five_sort(nums: List[int]) -> List[int]:
    # Approach: use 2 pointers, lp at start of list, rp at end of list to swap out 5
    # Ending condition: when both pointers meet each other

    lp, rp = 0, len(nums) - 1
    while lp < rp:
        if nums[lp] == 5:
            # swap with rp
            nums[lp], nums[rp] = nums[rp], nums[lp]
            # move rp
            rp -= 1
        else:
            lp += 1

    return nums


if __name__ == "__main__":
    example = [5, 2, 5, 6, 5, 1, 10, 2, 5, 5]
    ans = five_sort(example)
    print(ans)  # [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
