"""
Write a function fib that takes in a number argument, n, and returns the n-th number of the Fibonacci sequence.

The 0-th number of the sequence is 0.

The 1-st number of the sequence is 1.

To generate further numbers of the sequence, calculate the sum of previous two numbers.

Solve this recursively.
"""

from functools import lru_cache


@lru_cache()
def fib(n):
    if n == 1 or n == 0:
        return n

    return fib(n - 2) + fib(n - 1)


def fib_memoised(n):
    return _fib(n, {})


def _fib(n, memo):
    if n == 1 or n == 0:
        return n

    if n in memo:
        return memo[n]

    # store the value in the memo
    memo[n] = _fib(n - 1, memo) + _fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    res = fib(46)  # 1836311903, without lru_cache == timeout
    print(res)

    res2 = fib_memoised(46)
    print(res2)
