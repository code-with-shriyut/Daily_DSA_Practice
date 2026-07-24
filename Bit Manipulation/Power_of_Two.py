# LEETCODE 231: Power of Two

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An integer n is a power of two, if there exists an integer x such that n == 2x.

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1

# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16

# Example 3:

# Input: n = 3
# Output: false

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Power of 2 must be positive.
        if n <= 0:
            return False

        # Keep dividing by 2 until the number becomes odd.
        while n % 2 == 0:
            n //= 2

        # If we finally reach 1, it is a power of 2.
        return n == 1

# Time Complexity: O(log n)
# The number is divided by 2 in each iteration.

# Space Complexity: O(1)