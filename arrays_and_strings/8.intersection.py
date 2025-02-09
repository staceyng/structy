"""
Write a function, intersection, that takes in two lists, a,b, as arguments.
The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
"""

from typing import List


def intersection(a: List[int], b: List[int]) -> List[int]:
    set_a = set(a)
    result = []
    for i in b:
        if i in set_a:
            result.append(i)

    return result


if __name__ == "__main__":
    ans = intersection([4, 2, 1, 6], [3, 6, 9, 2, 10])
    print(ans)  # [2, 6]
