# ** Dictionary Consistency Checker **

# Problem Statement:
# A system stores data in a dictionary named records, where:
# Each key is a string.
# Each value is a list of integers.
# A key is said to be consistent if the list associated with it satisfies both condition.
# The list is strictly increasing.
# The difference between every pair of consecutive elements is the same.


# our task is to:
# Count how many keys in the dictionary are consistent.
# Print the count.

# Notes:
# A list with 0 or 1 element is considered consistent.
# You have to take the input.
# Print only an integer.

# code:

import ast

def is_consistent(lst):
    # Condition 1: list with 0 or 1 element
    if len(lst) <= 1:
        return True
    
    # Check strictly increasing
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    
    # Check equal differences
    diff = lst[1] - lst[0]
    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] != diff:
            return False
    
    return True

# Read input
records = ast.literal_eval(input())

count = 0

for key in records:
    if is_consistent(records[key]):
        count += 1

print(count)