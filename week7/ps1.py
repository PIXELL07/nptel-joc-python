# ** Problem Statement: Isomorphic Strings **

# You are given two strings s and t of equal length.
# Your task is to determine whether the two strings are isomorphic.

# Two strings are said to be isomorphic if characters in string s can be replaced to get string t, following these rules:
# Each character in s must map to exactly one character in t.
# All occurrences of a character must map to the same character.
# No two different characters in s can map to the same character in t.
# A character is allowed to map to itself.
# The order of characters must remain unchanged.

# If a valid one-to-one mapping exists, print true; otherwise, print false.

# Input Format:
# First line contains string s
# Second line contains string t

# Output Format:
# Print true if the strings are isomorphic
# Print false otherwise

# Constraints
# 1 ≤ length of s ≤ 10³
# length of s = length of t
# Strings contain only lowercase English letters

# Sample Explanation:
# For
# s = "egg"
# t = "add"
# e → a
# g → d

# The mapping is consistent and one-to-one, so the output is true.

# code:
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_map = {}
    t_map = {}

    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]

        # Check consistency in both directions
        if (char_s in s_map and s_map[char_s] != char_t) or \
           (char_t in t_map and t_map[char_t] != char_s):
            return False

        s_map[char_s] = char_t
        t_map[char_t] = char_s

    return True


# Input
s = input().strip()
t = input().strip()

# Output
print("true" if isIsomorphic(s, t) else "false")