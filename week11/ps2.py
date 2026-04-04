# ** Score Conservation Checker **

# You are given a directed graph and an initial score for each node through standard input.
# Your task is to perform one step of influence distribution using the same rules as Problem 1, and then check whether the total influence is conserved.

# Rules for influence distribution:
# 1) If a node has outgoing edges, it splits its score equally among its outgoing neighbors.
# 2) If a node has no outgoing edges, it keeps its entire score.
# 3) All incoming influence is accumulated.

# After performing one distribution step:
# Compute the sum of all node scores before distribution
# Compute the sum of all node scores after distribution
# Print True if the total score is conserved, otherwise print False

# Input Format;
# First line contains integer N — number of nodes

# Next N lines:
# Node followed by outgoing neighbors

# Next N lines:
# Node followed by its score

# Output Format:
# Print True if total score before and after distribution is the same
# Otherwise, print False

# code:

n = int(input())

# Read graph
graph = {}
for _ in range(n):
    parts = list(map(int, input().split()))
    node = parts[0]
    neighbors = parts[1:]
    graph[node] = neighbors

# Read scores
scores = {}
for _ in range(n):
    node, score = map(int, input().split())
    scores[node] = score

# Total before
total_before = sum(scores.values())

# Initialize new scores
new_scores = {node: 0 for node in scores}

# Distribute
for node in graph:
    if graph[node]:  # has outgoing edges
        share = scores[node] / len(graph[node])
        for neighbor in graph[node]:
            new_scores[neighbor] += share
    else:  # no outgoing edges
        new_scores[node] += scores[node]

# Total after
total_after = sum(new_scores.values())

# Check conservation
print(total_before == total_after)