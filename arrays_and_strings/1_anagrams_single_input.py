"""
Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether or not the strings are anagrams.
Anagrams are strings that contain the same characters, but in any order.
"""


def anagrams(s: str) -> bool:
    # Use 2 pointers approach, lp at start of string, rp at end of string
    # Loop condition to end when both pointers meet

    lp, rp = 0, len(s) - 1

    while lp < rp:
        if s[lp] != s[rp]:
            return False
        else:
            # increment both pointers
            lp += 1
            rp -= 1

    return True


if __name__ == "__main__":
    example1 = "kayak"
    example2 = "literally"
    ans = anagrams(example2)
    print(ans)
