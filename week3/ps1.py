# ** Problem Statement **

# At DataWorks, software systems rely on reusable list utility functions to safely extract elements from datasets without causing runtime errors.

# You are given a list L.

# Define the following Python functions:

# 1. safe_first(L)
#    - Returns the first element of the list L
#    - Returns None if the list is empty

# 2. safe_last(L)
#    - Returns the last element of the list L
#    - Returns None if the list is empty

# 3. safe_middle(L)
#    - Returns a list containing all elements except the first and last
#    - If the list is empty, return None
#    - If the list has one or two elements, return an empty list

# Constraints:
# - L may be empty
# - Elements of L can be integers or strings
# - Functions must not raise runtime errors

# code:

def safe_first(L):
    if not L:          # if L == [] :
        return None
    return L[0]

def safe_last(L):
    if not L:          # if L == [] :
        return None
    return L[-1]

def safe_middle(L):
    if not L:          # if L == [] :
        return None
    if len(L) <= 2:   
        return []
    return L[1:-1]

L = eval(input())

print(safe_middle(L))