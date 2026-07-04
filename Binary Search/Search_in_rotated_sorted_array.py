# LEETCODE 33: Search in Rotated Sorted Array

# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# APPROACH: Modified Binary Search

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        # Continue until the search space becomes empty
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid
            
            # Check if the left half is sorted
            if nums[left] <= nums[mid]:
                
                # Check if the target lies in the sorted left half 
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Otherwise, the right half must be sorted        
            else:
                 
                # Check if the target lies in the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
 
        # Target not found
        return -1
    
# Time Complexity: O(log n)
# - Binary Search reduces the search space by half in every iteration.

# Space Complexity: O(1)
# - Only a few variables are used.

# The Algorithm goes like:

    # Start Binary Search
    #         ↓
    # Find the middle element
    #         ↓
    # Is the target equal to nums[mid]?
    #         ↓
    # Yes → Return the index
    #         ↓
    # No
    #         ↓
    # Check which half is sorted
    #         ↓
    # Left half sorted?
    #         ↓
    # Yes
    #         ↓
    # Is the target inside the left half?
    #         ↓
    # Yes → Search left
    # No  → Search right
    #         ↓
    # Else
    #         ↓
    # Right half is sorted
    #         ↓
    # Is the target inside the right half?
    #         ↓
    # Yes → Search right
    # No  → Search left
    #         ↓
    # Repeat