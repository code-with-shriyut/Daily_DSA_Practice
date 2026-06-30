# Leetcode 18: 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Sort the array to apply the two-pointer approach
        nums.sort()

        # Store all unique quadruplets
        result = []

        # Fix the first element
        for i in range(len(nums) - 3):

            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Fix the second element
            for j in range(i + 1, len(nums) - 2):

                # Skip duplicate values for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Initialize two pointers
                left = j + 1
                right = len(nums) - 1

                # Search for the remaining two numbers
                while left < right:

                    # Calculate the sum of four numbers
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # If the target is found, save the quadruplet
                    if total == target:

                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Skip duplicate values from the left
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        # Skip duplicate values from the right
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        # Move both pointers to search for a new pair
                        left += 1
                        right -= 1

                    # Current sum is too small,
                    # move the left pointer to increase the sum
                    elif total < target:
                        left += 1

                    # Current sum is too large,
                    # move the right pointer to decrease the sum
                    else:
                        right -= 1

        # Return all unique quadruplets
        return result


# Time Complexity: O(n³)
# - Sorting takes O(n log n).
# - Two nested loops fix the first two numbers.
# - The two pointers scan the remaining array once.

# Space Complexity: O(1)
# - Only constant extra space is used (excluding the output list).