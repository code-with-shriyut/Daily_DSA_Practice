# LEETCODE 485: Max Consecutive Ones

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Store the current consecutive count of 1's
        current = 0

        # Store the maximum consecutive count of 1's found so far
        maximum = 0

        # Traverse the array
        for i in range(len(nums)):

            # If the current element is 1,
            # increase the current consecutive count
            if nums[i] == 1:
                current += 1

                # Update the maximum consecutive count if needed
                maximum = max(maximum, current)

            # If the current element is 0,
            # reset the current consecutive count
            else:
                current = 0

        # Return the maximum consecutive 1's
        return maximum


# Time Complexity: O(n)
# - Traverse the array only once.

# Space Complexity: O(1)
# - Only two variables are used.