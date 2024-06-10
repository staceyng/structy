def factorial(n: int) -> int:
    # base case
    if n <= 1:
        return 1

    return n * factorial(n - 1)


if __name__ == "__main__":
    ans = factorial(3)  # 1*2*3 = 6
    print(ans)
