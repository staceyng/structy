"""
Write a function, anagrams, that takes in two strings as arguments.
The function should return a boolean indicating whether or not the strings are anagrams.
Anagrams are strings that contain the same characters, but in any order.
"""


def anagrams(s1: str, s2: str) -> bool:
    # use dict to keep track of character map and count
    # if both dictionaries and count match == both strings are anagrams of each other
    # Time complexity: O(n+m)
    # Space complexity: O(n+m)

    s1_dict = {}
    for char in s1:
        if char not in s1_dict:
            s1_dict[char] = 1
        else:
            s1_dict[char] += 1

    s2_dict = {}
    for char in s2:
        if char not in s2_dict:
            s2_dict[char] = 1
        else:
            s2_dict[char] += 1

    return s2_dict == s1_dict


if __name__ == "__main__":
    example1 = "elbow"
    example2 = "yellow"
    ans = anagrams(example1, example2)
    print(ans)
