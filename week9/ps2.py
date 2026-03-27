# ** Pixel Intensity Quantizer **

# Problem Statement:
# You are given a set of pixel intensity values through standard input.
# Each pixel intensity is an integer between 0 and 255.
# Your task is to group these values into 8 discrete buckets based on the following rule:

# 0–31 → bucket 0

# 32–63 → bucket 1

# 64–95 → bucket 2

# 96–127 → bucket 3

# 128–159 → bucket 4

# 160–191 → bucket 5

# 192–223 → bucket 6

# 224–255 → bucket 7

# For each input value, determine its bucket and print the resulting list.

# Input Format:
# First line contains an integer n — number of intensity values
# Second line contains n space-separated integers representing pixel intensities

# Output Format:
# Print a list of integers representing the bucket value for each input intensity
# The order of elements must be preserved

# Constraints:
# 1 ≤ n ≤ 10⁵
# 0 ≤ intensity value ≤ 255

# code:

n = int(input().strip())
values = list(map(int, input().split()))

result = [v // 32 for v in values]

print(result)