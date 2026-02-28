# ** Recursive Digit Sum Calculator **

# Problem Statement
# To analyze numeric identifiers, systems often compute the sum of digits of a number. In this task, iterative approaches are restricted.
# You are required to write a Python function as described below.

# * digit_sum(n)

# Input:
# A non-negative integer n.

# Output:
# Return the sum of all digits of n.

# Notes:
# The solution must use recursion.
# Loops must NOT be used.
# The number must NOT be converted to a string.

# How it works:
# Base case: when n == 0, return 0
# Recursive step:
# n % 10 gets the last digit
# n // 10 removes the last digit
# Keep summing recursively

# code:

def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

# Example:

For digit_sum(123):

digit_sum(123)
= 3 + digit_sum(12)
= 3 + 2 + digit_sum(1)
= 3 + 2 + 1 + digit_sum(0)
= 6