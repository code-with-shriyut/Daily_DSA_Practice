# Find the sum of first N natural numbers using recursion.


class Solution(object):
    def sum_of_natural_numbers(self, n):
        if n == 1: # Base case: If n = 1, we return 1 as the sum of first natural number is 1 itself.
            return 1
        else: 
            return n + self.sum_of_natural_numbers(n-1) # We keep on calling the function recursively until we reach the base case where n = 1.
    
n = 5
print(Solution().sum_of_natural_numbers(n))

# Time complexity in this case is O(n) beacause we are having one recursive call for each value of n.
# Space complexity in this case is O(n) beacause we are using the call stack to store the recursive calls.