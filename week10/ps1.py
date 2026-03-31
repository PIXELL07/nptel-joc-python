# ** Character Reduction Game **

# Problem Statement:
# You are given two strings through standard input.
# Your task is to remove all common characters between the two strings by applying the following rule:
# If a character appears in both strings, remove one occurrence of that character from each string.
# This process continues until no common characters remain.
# After all possible removals, count the total number of remaining characters in both strings.
# Finally, print this total count.

# Input Format:
# First line contains string s1
# Second line contains string s2

# Output Format:
# Print a single integer representing the total number of remaining characters

# Constraints:
# 1 ≤ length of each string ≤ 10³
# Strings contain only lowercase English letters

# code:

# from collections import Counter
# s1 = input().strip()
# s2 = input().strip()

# c1 = Counter(s1)
# c2 = Counter(s2)

# result = 0

# # consider all unique characters
# all_chars = set(c1.keys()).union(set(c2.keys()))

# for ch in all_chars:
#     result += abs(c1[ch] - c2[ch])

# print(result)

# code: Simpler Version

from collections import Counter

s1 = input().strip()
s2 = input().strip()

print(sum((Counter(s1) - Counter(s2)).values()) +
      sum((Counter(s2) - Counter(s1)).values()))