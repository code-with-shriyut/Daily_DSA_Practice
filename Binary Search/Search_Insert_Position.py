# LeetCode 35
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid   #Target found, return it's index.
            elif nums[mid] < target:
                left  = mid + 1   # Target is greater, search right half.
            else:
                right = mid - 1   # Target is smaller, search left half.
        return left  # If target is not found, left points to the correct insertion position.

# Time Complexity in this case is O(log n) because we are dividing the array in half in each iteration.
# Space Complexity in this case is O(1) because no extra space is being used here.