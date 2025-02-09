"""
Write a function, factorial, that takes in a number n and returns the factorial of that number.
The factorial of n is the product of all the positive numbers less than or equal to n.
You must solve this recursively.

For example, the factorial of 6 is:
6 * 5 * 4 * 3 * 2 * 1 = 720

You can assume that n is a non-negative integer.
Note that the factorial of 0 is defined to be 1 
"""


def factorial(n: int) -> int:
    # base case
    if n <= 1:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    ans = factorial(3)  # 1*2*3 = 6
    print(ans)
