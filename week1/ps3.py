# ** Signal Stability Checker **
# Signal processors analyze sequences of numerical measurements to determine whether a signal is consistently increasing over time.

# ** Problem Description **
# You are given a sequence of integers representing signal measurements taken over time.
# A signal is said to be strictly increasing if every element is greater than the previous one.

# Input Format
# A single line containing space-separated integers representing signal measurements.

# Output Format
# Print True if the sequence is strictly increasing.

# Otherwise, print False.

# The program must always print exactly one Boolean value.

# * Constraints
# Input contains at least one integer.
# All values are integers.

# code

L = input().split()
nums = []

for x in L:
    nums.append(int(x))

flag = True

for i in range(len(nums) - 1):
    if nums[i] >= nums[i + 1]:
        flag = False
        break

print(flag)
