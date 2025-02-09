"""
Write a function, compress, that takes in a string as an argument.
The function should return a compressed version of the string where consecutive occurrences of the same characters are compressed into the number of occurrences followed by the character.
Single character occurrences should not be changed.

'aaa' compresses to '3a'
'cc' compresses to '2c'
't' should remain as 't'

You can assume that the input only contains alphabetic characters.
"""


def compress(s: str) -> str:
    # approach 2 pointers, lp to locate start, rp to locate end of character
    s += "!"  # mark the end of the string
    lp, rp = 0, 0
    final = ""

    while rp < len(s):
        if s[rp] == s[lp]:
            # move rp right
            rp += 1
        else:
            # different character is detected
            count = rp - lp
            print(count)
            final += f"{count}{s[lp]}"
            # update lp
            lp = rp

    return final


if __name__ == "__main__":
    """compress("ccaaat") # -> '2c3a1t'"""
    example = "ccaaat"
    ans = compress(example)
    print(ans)
