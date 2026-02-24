# ** Cargo Weight Floor Converter **

# Problem Statement
# At AeroPort-X, cargo weights are recorded as real numbers for logistical operations.
# For standardized loading, each recorded weight must be converted into an integer using a fixed rule.

# Task Description
# You are required to:

# 1) Accept a space-separated sequence of positive real numbers.

# 2) Convert each number to the greatest integer less than or equal to it.

# 3) Print the converted integers separated by commas.

# Input Format
# A single line containing space-separated real numbers.

# Output Format
# A single line containing integers separated by commas

# input:

# 1) 100.0 200.8
# 2) 7.7 8.8 9.9
# 3) 3.3 3.3 3.3

# 1) code:

import math
numbers = input().split()
floored = [str(math.floor(float(num))) for num in numbers]
print(",".join(floored))


# 2) code: 
# L = input().split()

# for i in range(len(L)):
#     L[i] = int(float(L[i]))

# for i in range(len(L)):
#     if i != len(L) - 1:
#         print(L[i], end=",")
#     else:
#         print(L[i])