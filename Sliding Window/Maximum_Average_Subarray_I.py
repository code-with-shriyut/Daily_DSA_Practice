# LEETCODE 643: Maximum Average Subarray I

# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

# APPROACH: Sliding Window

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Calculate the sum of the first window of size k
        window_sum = sum(nums[:k])

        # Initialize the maximum sum to the initial window sum
        max_sum = window_sum

        # Move the window one element at a time 
        for i in range(k, len(nums)):
            
            # Remove the leftmost element and add the new rightmost element
            window_sum = window_sum - nums[i - k] + nums[i]

            # Update the maximum sum if needed
            max_sum = max(max_sum, window_sum)
            
        # Return the maximum average
        return float(max_sum) / k
    
# Time Complexity: O(n)
# - The first window sum takes O(k).
# - The remaining windows are processed in O(n - k).
# - Overall complexity is O(n).

# Space Complexity: O(1)
# - Only a few variables are used.

# The Algorithm goes like:

    # Find the sum of the first window
    #         ↓
    # Store it as the maximum sum
    #         ↓
    # Move the window one step
    #         ↓
    # Subtract the element leaving the window
    #         ↓
    # Add the new element entering the window
    #         ↓
    # Update the maximum sum
    #         ↓
    # Repeat until the end
    #         ↓
    # Return maximum sum divided by k