"""
Write a function tribonacci that takes in a number argument, n, and returns the n-th number of the Tribonacci sequence.

The 0-th and 1-st numbers of the sequence are both 0.

The 2-nd number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous three numbers.

Solve this recursively.
"""


def tribonacci(n) -> int:
    return _tribonacci(n, {})


def _tribonacci(n, memo: dict) -> int:
    if n == 1 or n == 0:
        return 0

    if n == 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = (
        _tribonacci(n - 1, memo) + _tribonacci(n - 2, memo) + _tribonacci(n - 3, memo)
    )
    return memo[n]


if __name__ == "__main__":
    res = tribonacci(37)  # -> 1132436852
    print(res)
