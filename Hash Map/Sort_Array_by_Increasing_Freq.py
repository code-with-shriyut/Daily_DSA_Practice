# LEETCODE 1636: Sort Array by Increasing Frequency

# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.

# Example 1:

# Input: nums = [1,1,2,2,2,3]
# Output: [3,1,1,2,2,2]
# Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
# Example 2:

# Input: nums = [2,3,1,3,2]
# Output: [1,3,3,2,2]
# Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
# Example 3:

# Input: nums = [-1,1,-6,4,5,-6,1,4,1]
# Output: [5,-1,4,4,-6,-6,1,1,1]

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Store the frequency of each number
        freq = {}

        # Count the frequency of every number
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Sort the array:
        # 1. Increasing frequency
        # 2. If frequencies are equal, larger number comes first
        nums.sort(key=lambda x: (freq[x], -x))

        # Return the sorted array
        return nums


# Time Complexity: O(n log n)
# - Counting the frequencies takes O(n).
# - Sorting the array takes O(n log n).

# Space Complexity: O(n)
# - Dictionary stores the frequency of each number.