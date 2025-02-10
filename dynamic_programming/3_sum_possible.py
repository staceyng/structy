"""
Write a function sum_possible that takes in an amount and a list of positive numbers.
The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list.
You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
"""


def sum_possible(s: int, numbers: list) -> bool:
    return _sum_possible(s, numbers, {})


def _sum_possible(s: int, numbers: list, memo: dict) -> bool:
    # base case
    if s == 0:
        return True

    if s < 0:
        return False

    if s in memo:
        return memo[s]

    for n in numbers:
        res = _sum_possible(s - n, numbers, memo)

        if res is True:
            memo[s] = True
            return True

    memo[s] = False
    return False


if __name__ == "__main__":
    final = sum_possible(15, (6, 2, 10, 19))  # false
    print(final)
