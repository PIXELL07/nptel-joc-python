# ** Longest Consecutive Sequence Finder **

# Problem Statement:
# You are given a list of integers named nums.
# The integers may appear in any order and may include duplicates.

# Your task is to determine the length of the longest sequence of consecutive integers that can be formed using elements from the list.

# Important Notes:
# Consecutive numbers must differ by exactly 1.
# The sequence can be formed regardless of the order of elements in the list.
# Duplicate values should be considered only once.
# You must print only the length of the longest consecutive sequence.
# You need to take input.
# Do not use functions.

# Input Format:
# A list of integers nums (single line input).

# Example:
# [100, 4, 200, 1, 3, 2]

# Output Format:
# Print a single integer — the length of the longest consecutive sequence.

# code:

nums = list(map(int, input().strip('[]').replace(',', ' ').split()))

num_set = set(nums)
longest = 0

for num in num_set:
    if num - 1 not in num_set:  # start of sequence
        current = num
        length = 1

        while current + 1 in num_set:
            current += 1
            length += 1

        longest = max(longest, length)

print(longest)