#Count Disjoint Pairs Whose Sum is Divisible by T

# Problem Statement:
# Given an array of integers and an integer T, count the number of disjoint pairs such that:

# The sum of each pair is an exact multiple of T.
# Each element in the array can be used only once.

# Example:

# Input:
# Array = [3, 7, 13, -3, 5]
# T = 10

# Output:
# 2

# Explanation:
# Valid disjoint pairs are:
# (3, 7)  → 10 (divisible by 10)
# (13, -3) → 10 (divisible by 10)

# 5 remains unused.

# Number of elements
n = int(input())

# Array
arr = list(map(int, input().split()))

# Value of T
T = int(input())

# Stores frequency of remainders
freq = {}

# Stores total number of valid pairs
count = 0

for num in arr:

    # Find remainder
    remainder = num % T

    # Find the remainder needed to make the sum divisible by T
    complement = (T - remainder) % T

    # If a suitable remainder already exists,
    # make a pair
    if freq.get(complement, 0) > 0:

        count += 1
        freq[complement] -= 1

    # Otherwise store the current remainder
    else:
        freq[remainder] = freq.get(remainder, 0) + 1

print(count)

# Time Complexity: O(n)
# - Traverse the array only once.
# - Each HashMap operation takes O(1) on average.

# Space Complexity: O(T)
# - At most T different remainders (0 to T-1)
#   are stored in the HashMap.