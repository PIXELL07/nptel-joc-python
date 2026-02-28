# ** Recursive Minimum Finder **

# Problem Statement
# Recursive algorithms are often used to process lists when iteration is restricted.
# You are required to write a Python function as described below.

# * recursive_min(L)

# Input:
# A non-empty list of integers L.

# Output:
# Return the minimum element present in the list.

# Notes:
# The solution must use recursion.
# Loops must NOT be used.
# The built-in min() function must NOT be used.

# How it works
# Base case: one element → that element is the minimum

# Recursive step:
# Find the minimum of the rest of the list
# Compare it with the first element
# Return the smaller value

# code:

def recursive_min(L):
    if len(L) == 1:
        return L[0]
    
    rest_min = recursive_min(L[1:])
    
    if L[0] < rest_min:
        return L[0]
    else:
        return rest_min