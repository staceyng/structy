def uncompress(s: str) -> str:
    # Approach 2 pointers, lp at start of number rp to find end of number
    base_numbers = "0123456789"
    lp, rp = 0, 0
    final = ""

    while rp < len(s):
        if s[rp] in base_numbers:
            # rp is a number
            rp += 1
        else:
            # rp is a letter
            num = int(s[lp:rp])
            char = s[rp]
            final += num * char

            # update rp and lp
            rp += 1
            lp = rp
    return final


if __name__ == "__main__":
    """uncompress("2c3a1t") # -> 'ccaaat'"""
    example = "2c3a1t"
    ans = uncompress(example)
    print(ans)
