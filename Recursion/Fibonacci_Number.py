# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 1: # Base case: If n is less than or equal to 1, we return n as the Fibonacci number for that position is n itself.
            return n
        else:
            return self.fib(n-1) + self.fib(n-2) # We keep on calling the function recusrively until we reach the base case where n is less than or equal to 1.
        
n = 5
print(Solution().fib(n))

# Time complexity in this case is O(2^n) beacause we are having two recursive calls for each value of n.
# Space complexity in this case is O(n) because we are using the call stack to store the recursive calls.