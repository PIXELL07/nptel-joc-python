# ** Energy Readings at Solar Valley **

# At Solar Valley Research Station, engineers record daily energy readings from solar panels. Each reading represents the amount of power generated on a particular day. To assess performance, analysts compare individual readings against the overall average.

# Problem Statement
# Given a sequence of daily energy readings, determine how many readings are strictly greater than the average of all readings.

# Input Format
# A single line containing space-separated positive integers (each integer represents the energy generated on a day).


# Output Format
# Print a single integer:
# the count of numbers strictly greater than the average of the given sequence.

# Constraints

# - All input numbers are positive integers.
# - At least one number is present in the input.

# Computation Details

# 1) Compute the average of all given numbers.
# 2) Count how many numbers are greater than (not equal to) the average.
# 3) Print the count.

# Sample Input
# 10 20 30 40 50

# Sample Output
# 2

# code:

L = input().split()

nums = []
for x in L:
    nums.append(int(x))

total = 0
for x in nums:
    total += x

avg = total / len(nums)

count = 0
for x in nums:
    if x > avg:
        count += 1

print(count)
