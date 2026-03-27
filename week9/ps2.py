# ** Circular Elimination Game **

# Problem Statement:

# You are given a group of players arranged in a circle.
# Starting from the first player, every k-th player is eliminated in a circular manner.
# The elimination continues until only one player remains.
# Your task is to simulate this process using the given inputs and determine the position (1-indexed) of the last remaining player.

# Input Format:
# First line contains an integer n — the number of players
# Second line contains an integer k — the step count for elimination

# Output Format:
# Print a single integer representing the position of the last remaining player

# Constraints:
# 1 ≤ n ≤ 10⁵
# 1 ≤ k ≤ 10⁵

# code:

def josephus(n, k):
    result = 0  # 0-based index
    for i in range(1, n + 1):
        result = (result + k) % i
    return result + 1  # convert to 1-based index

# Input
n = int(input().strip())
k = int(input().strip())

# Output
print(josephus(n, k))