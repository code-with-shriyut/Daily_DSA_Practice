# LEETCODE 167: Two Sum II

# #Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

class Solution:
    def twoSum(self, numbers: List[int], target: int):

        # Initialize two pointers at both ends of the sorted array
        i = 0
        j = len(numbers) - 1

        # Continue until the two pointers meet
        while i < j:

            # Calculate the sum of the current pair
            current_sum = numbers[i] + numbers[j]

            # Target found, return 1-based indices
            if current_sum == target:
                return [i + 1, j + 1]

            # Sum is too large, move the right pointer left
            elif current_sum > target:
                j -= 1

            # Sum is too small, move the left pointer right
            else:
                i += 1

# Time Complexity: O(n)
# - Each pointer moves at most n times.
# - The array is traversed only once.

# Space Complexity: O(1)
# - Only two pointers are used.
# - No extra data structure is required.

# Approach:
#
# Since the array is already sorted, use two pointers.
#
# - Place one pointer at the beginning and the other at the end.
# - Calculate the sum of the two elements.
#
# 1. If the sum equals the target,
#    return their 1-based indices.
#
# 2. If the sum is greater than the target,
#    move the right pointer left to decrease the sum.
#
# 3. If the sum is smaller than the target,
#    move the left pointer right to increase the sum.
#
# Repeat until the target pair is found.
