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
