# ** Word Length Comparator **

# Problem Statement:

# Text analysts compare words based on their lengths. Write a program to perform the following steps:

# 1) Accept a comma-separated list of words.
# 2) Calculate the average length of the words.
# 3) Round up the average to the nearest whole number (Ceiling value).
# 4) Count how many words have a length strictly greater than this rounded average.

# Input Format:
# A single line containing comma-separated words.

# Output Format:
# Print a single integer count.

# Example Calculation (for clarity):
# -- Input: one,two,three,four
# -- Word Lengths: 3, 3, 5, 4
# -- Mathematical Average: (3+3+5+4) / 4 = 3.75
# -- Rounded Average (Ceiling): 4 (Always round up decimal values)
# -- Comparison: Check which words have length > 4.

# one (3) > 4? No.
# two (3) > 4? No.
# three (5) > 4? Yes.
# four (4) > 4? No.


# code:

import math

L = input().split(',')

total = 0
for w in L:
    total += len(w)

avg = math.ceil(total / len(L))

count = 0
for w in L:
    if len(w) > avg:
        count += 1

print(count)