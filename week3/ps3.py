# ** Problem Statement **

# Data validation systems often need to detect duplicate values in datasets to ensure data integrity.

# Write a function has_duplicates(L) that:
# - Accepts a list L
# - Returns True if any element appears more than once
# - Returns False if all elements are unique

# Constraints:
# - L may be empty
# - Elements can be integers or strings

# input:
# [9,8,7,9]
# [0,1,2,3,4]
# ["a","b","a"]

# code:

def has_duplicates(L):
    seen = []
    for x in L:
        if x in seen:
            return True
        seen.append(x)
    return False
L = eval(input())
print(has_duplicates(L))