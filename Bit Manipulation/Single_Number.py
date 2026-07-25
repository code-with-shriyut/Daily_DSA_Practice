# LEETCODE 136: Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize the result variable to 0.
        # XOR with 0 returns the number itself.
        ans = 0

        # Traverse through every element in the array.
        for num in nums:
            # XOR the current element with the accumulated result.
            #
            # Properties of XOR:
            # 1. a ^ a = 0  (same numbers cancel each other)
            # 2. a ^ 0 = a  (XOR with 0 returns the number)
            # 3. XOR is commutative and associative.
            #
            # Since every element appears twice except one,
            # all duplicate elements cancel out, leaving only
            # the unique element.
            ans ^= num

        # Return the element that appears only once.
        return ans


# Time Complexity: O(n)
# - We traverse the array exactly once.

# Space Complexity: O(1)
# - Only one extra variable (ans) is used, regardless of input size.
