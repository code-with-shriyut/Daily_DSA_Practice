# LEETCODE 1512: Number of Good Pairs

# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:

# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# Example 2:

# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# Example 3:

# Input: nums = [1,2,3]
# Output: 0

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Store the frequency of each number
        freq = {}

        # Store the total number of good pairs
        pairs = 0

        # Traverse the array
        for num in nums:

            # If the number has been seen before
            # it forms 'freq[num]' new pairs
            if num in freq:
                pairs += freq[num]

            # Increase the frequency of the current number
            freq[num] = freq.get(num, 0) + 1

        # Return the total number of good pairs
        return pairs

# Time Complexity: O(n)
# - Traverse the array only once.

# Space Complexity: O(n)
# - Dictionary stores the frequency of each number.