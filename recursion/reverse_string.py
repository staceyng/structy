def reverse_string(s: str):
    # base case
    if len(s) == 0:
        return ""

    return s[-1] + reverse_string(s[:-1])


if __name__ == "__main__":
    example = "hello"
    ans = reverse_string(example)  # olleh
    print(ans)
