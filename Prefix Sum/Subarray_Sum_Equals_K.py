# LEETCODE 560: Subarray Sum Equals K

# Given an array of integers nums and an integer k, 
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Store the total number of valid subarrays
        count = 0

        # Store the running prefix sum
        current_sum = 0

        # Store the frequency of each prefix sum
        hashmap = {0: 1}

        # Traverse the array
        for num in nums:

            # Update the running prefix sum
            current_sum += num

            # If (current_sum - k) exists,
            # add its frequency to the answer
            if current_sum - k in hashmap:
                count += hashmap[current_sum - k]

            # Store/update the frequency of the current prefix sum
            if current_sum in hashmap:
                hashmap[current_sum] += 1
            else:
                hashmap[current_sum] = 1

        # Return the total number of valid subarrays
        return count


# Time Complexity: O(n)
# - Traverse the array only once.

# Space Complexity: O(n)
# - HashMap stores the prefix sums and their frequencies.

# How it Works?!

# Update current_sum
#         ↓
# Can I find current_sum - k?
#         ↓
# YES → Increase count

# NO  → Nothing happens
#         ↓
# Store current_sum in the hashmap
#         ↓
# Move to the next number