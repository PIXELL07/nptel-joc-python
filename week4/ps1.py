# ** Divisor Archive of Mathoria **

# Problem Statement
# In the land of Mathoria, scholars study numbers by analyzing their divisors. You are required to write three Python functions as described below.

# 1. divisors(n)

# Input:
# An integer n where n ≥ 1.
# Output:
# Return a sorted list of all positive divisors of n.
# Notes:
# The list must be in ascending order.
# Each divisor should appear exactly once.

# 2. common_divisors(a, b)

# Input:
# Two integers a and b where a ≥ 1 and b ≥ 1.
# Output:
# Return a sorted list of all common positive divisors of a and b.
# Notes:
# The list must be in ascending order.
# The result must be a list, not a set or tuple.

# 3. divisors_upto(n)

# Input:
# An integer n where n ≥ 1.
# Output:
# Return a dictionary in which:
# Each key is an integer from 1 to n (inclusive).
# Each value is a sorted list of all positive divisors of the key.
# Notes:
# Dictionary keys must appear in increasing order from 1 to n.
# Each value must follow the same rules as the output of divisors(n).

# Example Behaviour (for clarity)

# divisors(6) → [1, 2, 3, 6]
# common_divisors(12, 18) → [1, 2, 3, 6]
# divisors_upto(3) → {1: [1], 2: [1, 2], 3: [1, 3]}

# code:

def divisors(n):
    result = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
        i += 1
    result.sort()
    return result

def common_divisors(a, b):
    da = divisors(a)
    db = divisors(b)
    result = []
    for x in da:
        if x in db:
            result.append(x)
    return result

def divisors_upto(n):
    d = {}
    for i in range(1, n + 1):
        d[i] = divisors(i)
    return d
  