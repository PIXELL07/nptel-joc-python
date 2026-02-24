# ** Problem Statement **

# A perfect number is a positive integer that is equal to the sum of its proper divisors (excluding the number itself).

# Write a function is_perfect(n) that:

# - Accepts a positive integer n
# - Returns True if n is a perfect number
# - Returns False otherwise

# Constraints:
# - 1 ≤ n ≤ 10^6
# - n is an integer

# input: 496,10,2

# def is_perfect(n):
#     if n <= 1:
#         return False
    
#     total = 1  
    
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             total += i
#             if i != n // i:  
#                 total += n // i
    
#     return total == n

# n = int(input())
# print(is_perfect(n))

# code:

def is_perfect(n):                        
    if n <= 1:
        return False

    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i

    return s == n
n = int(input())
print(is_perfect(n))
