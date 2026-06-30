# Leetcode 16: 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # Sort the array
        nums.sort()

        # Assume the first three numbers give the closest sum
        closest = nums[0] + nums[1] + nums[2]

        # Fix one element
        for i in range(len(nums) - 2):

            left = i + 1
            right = len(nums) - 1

            # Search for the best pair
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # Update the closest sum if the current sum is closer
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Perfect match found
                if total == target:
                    return total

                # Need a larger sum
                elif total < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        # Return the closest sum
        return closest
    
# Time Complexity: O(n²)

# Space Complexity: O(1)
