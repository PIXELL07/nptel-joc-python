# ** Problem Statement: Valid Anagram **

# You are given two strings s and t.
# Your task is to determine whether string t is an anagram of string s.

# Two strings are anagrams if:
# They contain the same characters
# Each character appears the same number of times in both strings
# The order of characters does not matter
# If t is an anagram of s, print true.
# Otherwise, print false.

# Input Format:
# First line contains string s
# Second line contains string t

# Output Format:
# Print true if t is an anagram of s
# Print false otherwise

# Constraints
# 1 ≤ length of s, t ≤ 5 × 10⁴

# Strings contain only lowercase English letters

# code:
def isAnagram(s, t):
    # If lengths differ, cannot be anagrams
    if len(s) != len(t):
        return False

    count = {}

    # Count characters in s
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # Subtract counts using t
    for ch in t:
        if ch not in count or count[ch] == 0:
            return False
        count[ch] -= 1

    return True


# Input
s = input().strip()
t = input().strip()

# Output
print("true" if isAnagram(s, t) else "false")