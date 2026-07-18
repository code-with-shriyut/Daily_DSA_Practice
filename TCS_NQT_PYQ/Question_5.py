## Prime Factorization of a Number ##

# Problem Statement:
# Given a positive integer N, print all of its prime factors in increasing order.
# If a prime factor occurs multiple times, print it multiple times.

# Input Format
# A single integer N.
# Output Format:
# Print the prime factors of N separated by spaces.
# Constraints:
# 2≤N≤10^9

# Example 1
# Input
# 60
# Output
# 2 2 3 5
# Explanation
# 60 = 2 × 2 × 3 × 5

# Example 2
# Input
# 13
# Output
# 13
# Explanation
# 13 is itself a prime number.

# SOLUTION:

# Input the number
n = int(input())

# Start checking factors from 2
i = 2

# Continue until i * i is less than or equal to n
while i * i <= n:

    # If i divides n, then i is a prime factor
    while n % i == 0:
        print(i, end=" ")

        # Remove this factor from n
        n = n // i

    # Check the next possible factor
    i += 1

# After removing all smaller prime factors, if n > 1, it is itself a prime factor
if n > 1:
    print(n)

# Time Complexity: O(√N)
# We check factors only up to the square root of N.

# Space Complexity: O(1)
# Only a few extra variables are used.