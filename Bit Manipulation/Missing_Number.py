# LEETCODE 268: Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]

# Output: 2

# Explanation:

# n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# Example 2:

# Input: nums = [0,1]

# Output: 2

# Explanation:

# n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

# LEETCODE 268: Missing Number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Start with the value 'n' because the loop will only cover 0 to n-1
        xor = len(nums)

        # XOR all indices and array elements
        for i in range(len(nums)):

            # XOR with the current index
            xor ^= i

            # XOR with the current array element
            xor ^= nums[i]

        # After all duplicate numbers cancel out,
        # the remaining value is the missing number
        return xor


# Time Complexity: O(n)
# - Traverse the array only once.

# Space Complexity: O(1)
# - Only one variable is used.
