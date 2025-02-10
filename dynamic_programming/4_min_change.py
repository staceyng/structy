"""
Write a function min_change that takes in an amount and a list of coins.
The function should return the minimum number of coins required to create the amount.
You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1.
"""


def min_change(amt: int, coins: list) -> int:
    ans = _min_change(amt, coins, {})
    if ans == float("inf"):
        return -1
    else:
        return ans


def _min_change(amt: int, coins: list, memo: dict) -> int:
    if amt in memo:
        return memo[amt]

    if amt == 0:
        return 0

    if amt < 0:
        return float("inf")

    min_coin_count = float("inf")
    for c in coins:
        cal = 1 + _min_change(amt - c, coins, memo)
        min_coin_count = min(min_coin_count, cal)

    memo[amt] = min_coin_count
    return min_coin_count


if __name__ == "__main__":
    res = min_change(8, [1, 5, 4, 12])
    print(res)  # 2, 4+4 is minimum coins possible
