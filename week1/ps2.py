# ** Temperature Alert System **

# ClimateWatch monitors daily temperature readings collected from different regions.
# To ensure safety, the system must flag temperatures that exceed the permissible limit.

# ** Problem Description **

# You are given a single line of input containing space-separated integers, where each integer represents a temperature reading for a particular region.
# A temperature is considered unsafe if it is strictly greater than 50.

# Input Format
# A single line containing space-separated integers representing temperature readings.

# Output Format
# If one or more temperatures are strictly greater than 50, print all such temperatures in the same order as input, separated by spaces.

# If no temperature exceeds 50, print 0.

# code

L = input().split()
result = []

for x in L:
    if int(x) > 50:
        result.append(x)

if len(result) == 0:
    print(0)
else:
    print(" ".join(result))
    