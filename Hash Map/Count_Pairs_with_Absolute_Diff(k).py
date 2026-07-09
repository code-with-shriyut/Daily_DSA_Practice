# LEETCODE 2006: Count Number of Pairs With Absolute Difference K

# Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.
# The value of |x| is defined as:
# x if x >= 0.
# -x if x < 0.
 
# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# Example 2:

# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.
# Example 3:

# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Store the frequency of the numbers seen so far
        freq = {}

        # Store the total number of valid pairs
        pairs = 0

        # Traverse the array
        for num in nums:

            # Check if there is a previously seen numer
            # whose difference with the current number is k
            if num - k in freq:
                pairs += freq[num - k]
            
            # Check for the other possible value
            # whose difference with the current number is k
            if num + k in freq:
                pairs += freq[num + k]

            # Store the frequency of the current number  
            freq[num] = freq.get(num, 0) + 1
        
        # Return the total number of pairs
        return pairs
    
# Time Complexity: O(n)
# - Traverse the array only once.
# - Dictionary lookups take O(1) on average.

# Space Complexity: O(n)
# - Dictionary stores the frequency of the numbers.