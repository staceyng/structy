"""
Write a function, most_frequent_char, that takes in a string as an argument.
The function should return the most frequent character of the string.
If there are ties, return the character that appears earlier in the string.

You can assume that the input string is non-empty.
"""

from collections import Counter


def most_frequent_char(s: str) -> str:
    # approach: 1st loop to loop through entire string to form a dictionary
    # 2nd loop to find max count of letter
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    current_max = 0
    freq_char = ""
    for k, v in dict(Counter(s)).items():
        if v > current_max:
            current_max = v
            freq_char = k

    return freq_char


if __name__ == "__main__":
    example = "mississippi"  # s
    ans = most_frequent_char(example)
    print(ans)
