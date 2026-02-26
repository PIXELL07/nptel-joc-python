# ** Recursive Multiplication Engine **

# Problem Statement

# In embedded systems at RoboLabs, direct multiplication hardware is unavailable. Engineers must rely on recursive logic based on repeated addition to compute products.
# You are required to write a Python function as described below.

# 1. multiply(a, b)
# Input:
# Two non-negative integers a and b.

# Output:
# Return the product a × b.

# Notes:

# The computation must be done using recursion.
# Only addition and subtraction may be used.
# Loops (for, while) must NOT be used.
# The * operator must NOT be used.

# code 1:

# Why this works :
# Uses recursion only
# Uses addition and subtraction only
# No *, for, or while
# Correct for all non-negative integers

def multiply(a, b):   
    # Base case: anything times 0 is 0
    if b == 0:
        return 0
    
    # Recursive case: a * b = a + a * (b - 1)
    return a + multiply(a, b - 1)

# code 2: this works too :
# Optional optimization (same rules, faster for large numbers):

def multiply(a, b):
    if b == 0:
        return 0
    if b == 1:
        return a
    if b % 2 == 0:
        half = multiply(a, b // 2)
        return half + half
    else:
        return a + multiply(a, b - 1)