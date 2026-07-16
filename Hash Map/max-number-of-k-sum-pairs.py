# LEETCODE 1679: Max Number of K-Sum Pairs

# You are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k 
# and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Example 1:

# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
# Example 2:

# Input: nums = [3,1,3,4,3], k = 6
# Output: 1
# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.


class Solution:
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Stores the frequency of numbers
        frequency = {}

        # Stores the total number of valid pairs
        count = 0

        # Traverse every number in the array
        for num in nums:

            # Find the number needed to make the sum equal to k
            complement = k - num

            # If the required number is already available,
            # make a pair
            if frequency.get(complement, 0) > 0:

                count += 1
                frequency[complement] -= 1

            # Otherwise, store the current number
            # for future pairing
            else:
                frequency[num] = frequency.get(num, 0) + 1

        # Return the maximum number of pairs
        return count


# Time Complexity: O(n)
# - Traverse the array only once.
# - Each HashMap operation takes O(1) on average.

# Space Complexity: O(n)
# - In the worst case, every element may be stored in the HashMap.
 