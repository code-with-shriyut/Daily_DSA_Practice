# LEETCODE 55: Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, 
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, 
# which makes it impossible to reach the last index.

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # Initially, our goal is the last index
        goal = len(nums) - 1

        # Traverse the array from right to left
        for i in range(len(nums) - 2, -1, -1):

            # If the current index can reach the goal,
            # move the goal to the current index
            if i + nums[i] >= goal:
                goal = i

        # If the goal becomes the first index,
        # we can reach the last index
        return goal == 0
    
# Time Complexity: O(n)
# - Traverse the array only once.

# Space Complexity: O(1)
# - Only one variable (goal) is used.