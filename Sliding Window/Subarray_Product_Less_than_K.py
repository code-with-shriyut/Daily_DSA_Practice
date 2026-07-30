# LEETCODE 713: Subarray Product Less than K

# Given an array of integers nums and an integer k, 
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# Example 1:

# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
# Example 2:

# Input: nums = [1,2,3], k = 0
# Output: 0
 
# Constraints:
# 1 <= nums.length <= 3 * 104
# 1 <= nums[i] <= 1000
# 0 <= k <= 106

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int):

        # If k is 0 or 1, no valid subarray is possible
        if k <= 1:
            return 0

        # Left boundary of the sliding window
        left = 0

        # Stores the product of the current window
        product = 1

        # Counts the total number of valid subarrays
        count = 0

        # Expand the window by moving the right pointer
        for right in range(len(nums)):

            # Include the current element in the product
            product *= nums[right]

            # Shrink the window until the product becomes less than k
            while product >= k:
                product /= nums[left]
                left += 1

            # Count all valid subarrays ending at 'right'
            count += right - left + 1

        # Return the total number of valid subarrays
        return count
    
# Time Complexity: O(n)
# - Each element enters and leaves the sliding window at most once.

# Space Complexity: O(1)
# - Only a few variables are used.
# - No extra data structure is required.

# Approach:
#
# Use the Sliding Window technique.
#
# Maintain a window whose product is always less than k.
#
# - Expand the window by moving the right pointer
#   and multiply the current element into the product.
#
# - If the product becomes greater than or equal to k,
#   shrink the window from the left until the product
#   is less than k again.
#
# - Once the window is valid, every subarray ending at
#   the current right pointer is also valid.
#
# Number of such subarrays:
#
#     right - left + 1
#
# Add this value to the answer.