# ** Problem Statement: Longest Common Prefix **

# You are given N strings.
# Your task is to find the longest common prefix shared among all the given strings.
# A prefix is a sequence of characters that appears at the beginning of each string.
# If no common prefix exists, print an empty string "".

# Input Format:
# First line contains an integer N — the number of strings
# The next N lines each contain one string

# Output Format:
# Print the longest common prefix
# If no common prefix exists, print an empty string ""

# Constraints:
# 1 ≤ N ≤ 200
# 1 ≤ length of each string ≤ 200
# Strings contain only lowercase English letters

# code:

n = int(input())
strings = [input().strip() for _ in range(n)]

prefix = min(strings)
suffix = max(strings)

i = 0
while i < len(prefix) and prefix[i] == suffix[i]:
    i += 1

result = prefix[:i]
print(result if result else '""')