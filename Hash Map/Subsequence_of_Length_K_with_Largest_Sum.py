# LEETCODE 2099: Find Subsequence of Length K With the Largest Sum

# You are given an integer array nums and an integer k. 
# You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some 
# or no elements without changing the order of the remaining elements.

# Example 1:

# Input: nums = [2,1,3,3], k = 2
# Output: [3,3]
# Explanation:
# The subsequence has the largest sum of 3 + 3 = 6.
# Example 2:

# Input: nums = [-1,-2,3,4], k = 3
# Output: [-1,3,4]
# Explanation: 
# The subsequence has the largest sum of -1 + 3 + 4 = 6.
# Example 3:

# Input: nums = [3,4,3,3], k = 2
# Output: [3,4]
# Explanation:
# The subsequence has the largest sum of 3 + 4 = 7. 
# Another possible subsequence is [4, 3].

class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Create a sorted copy of the original array
        sorted_nums = sorted(nums)

        # Store the frequency of the largest k elements
        freq = {}

        # Traverse only the largest k elements
        for num in sorted_nums[-k:]:

            # Count how many times each selected number appears
            freq[num] = freq.get(num, 0) + 1

        # Store the final subsequence
        result = []

        # Traverse the original array to preserve the original order
        for num in nums:

            # If the current number is still required,
            # add it to the answer
            if freq.get(num, 0) > 0:

                result.append(num)

                # Decrease its remaining frequency
                freq[num] -= 1

        # Return the required subsequence
        return result


# Time Complexity: O(n log n)
# - Sorting takes O(n log n).
# - Building the frequency map takes O(k).
# - Traversing the original array takes O(n).

# Space Complexity: O(n)
# - Sorted copy uses O(n) space.
# - Frequency dictionary uses at most O(k) space.
# - Result array stores k elements.