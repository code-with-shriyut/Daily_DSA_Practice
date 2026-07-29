# LEETCODE 1004: Max Consecutive Ones III

# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 
# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeroCount = 0
        maxLength = 0

        # Right pointer expands the window
        for right in range(len(nums)):

            # If current element is 0, include it in the window
            if nums[right] == 0:
                zeroCount += 1

            # Shrink the window until it becomes valid
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1

            # Window is valid, update the answer
            maxLength = max(maxLength, right - left + 1)

        return maxLength

# Time Complexity: O(n)
# - Each element is visited at most twice:
#   once by the right pointer and once by the left pointer.

# Space Complexity: O(1)
# - Only a few variables are used.
# - No extra data structure is required.

# Approach:
#
# Use the Sliding Window technique.
#
# Expand the window by moving the right pointer.
#
# Count the number of zeros in the current window.
#
# - If zeroCount <= k:
#     The window is valid, so update the maximum length.
#
# - If zeroCount > k:
#     Shrink the window from the left until
#     the number of zeros becomes at most k.
#
# Continue until the end of the array.