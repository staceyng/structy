def palindrome(s: str) -> bool:
    # base case
    if len(s) <= 1:
        return True

    # check first letter and end letter to see if they match
    if s[0] == s[-1]:
        # remove from string
        s = s[1:-1]
        return palindrome(s[1:-1])
    else:
        return False


if __name__ == "__main__":
    example1 = "kayak"
    ans = palindrome(example1)
    print(ans)
