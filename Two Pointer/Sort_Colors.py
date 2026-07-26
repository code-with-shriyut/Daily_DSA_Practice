# LEETCODE 75: Sort Colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, 
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

class Solution:
    def sortZeroOneTwo(self, nums):

        # Three pointers
        low, mid, high = 0, 0, len(nums) - 1

        # Process elements until mid crosses high
        while mid <= high:

            # Move 0 to the left side
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            # Leave 1 in the middle
            elif nums[mid] == 1:
                mid += 1

            # Move 2 to the right side
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# Time Complexity: O(n)
# - We traverse the array only once.
# - Every element is processed at most one time.

# Space Complexity: O(1)
# - The array is sorted in-place.
# - Only three variables (low, mid, high) are used.

# We divide the array into four regions:
#
#  -------------------------------------------------
#  |   0s   |   1s   | Unsorted |      2s          |
#  -------------------------------------------------
#      ^        ^         ^              ^
#     low      mid       ...           high
#
# Initially:
# - low = 0
# - mid = 0
# - high = last index
#
# We inspect the element at the 'mid' pointer.
#
# 1. If nums[mid] == 0:
#    - Swap it with nums[low] because 0 belongs to the left side.
#    - Increase both low and mid.
#
# 2. If nums[mid] == 1:
#    - 1 is already in its correct middle region.
#    - Just move mid forward.
#
# 3. If nums[mid] == 2:
#    - Swap it with nums[high] because 2 belongs to the right side.
#    - Decrease high only.
#    - Do NOT move mid because the swapped element
#      from the right has not been checked yet.
#
# Continue until mid crosses high.
# At the end, all 0s are on the left,
# all 1s are in the middle,
# and all 2s are on the right.