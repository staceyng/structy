def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    ans = fibonacci(4)  # 1
    print(ans)
