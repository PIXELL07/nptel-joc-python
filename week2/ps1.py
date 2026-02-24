# The Shortest Codeword of Lexicon City
# Problem Statement
# In Lexicon City, encrypted messages are stored as comma-separated words.You are required to identify a special word based on the following rules:

# 1) Accept a comma-separated list of words as input.

# 2) Find the word with the minimum length.

# 3) If multiple words share the same minimum length, print the rightmost such word.

# Input Format
# A single line containing comma-separated words.

# Output Format
# Print the required word.


# Test Case 1	   # Test Case 2             # Test Case 3
# input: x,y,z     input: red,blue,green      input: one,two,ten
# output: z        output: red                output: ten
# z\n              red\n                      ten\n
 

# ex :

# words = input().split(',')

# words = [word.strip() for word in words]

# min_length = min(len(word) for word in words)

# for word in reversed(words):
#     if len(word) == min_length:
#         print(word)
#         break

# code :

L = input().split(',')

min_word = L[0]
min_len = len(L[0])

for w in L:
    if len(w) <= min_len:
        min_len = len(w)
        min_word = w

print(min_word)