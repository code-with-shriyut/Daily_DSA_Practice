# LEETCODE 442: Find All Duplicates in an Array

# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, 
# return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []


class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Store all duplicate numbers
        result = []

        # Traverse the array
        for num in nums:

            # Find the corresponding index
            index = abs(num) - 1

            # If the value at this index is already negative,
            # the current number is a duplicate
            if nums[index] < 0:
                result.append(abs(num))

            # Otherwise, mark this index as visited
            else:
                nums[index] = -nums[index]

        # Return all duplicates
        return result


# Time Complexity: O(n)
# - Traverse the array only once.

# Space Complexity: O(1)
# - No extra data structure is used (excluding the output array).