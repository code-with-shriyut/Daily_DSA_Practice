# LEETCODE 350: Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Store the frequency of each element in nums1
        freq = {}

        for num in nums1:
            freq[num] = freq.get(num, 0) + 1

        # Store the common elements (including duplicates)
        result = []

        # Traverse nums2
        for num in nums2:

            # If the element exists and its frequency is greater than 0
            if num in freq and freq[num] > 0:

                # Add the element to the answer
                result.append(num)

                # Decrease its frequency
                freq[num] -= 1

        # Return the intersection
        return result


# Time Complexity: O(n + m)
# - Traverse nums1 once to build the frequency map.
# - Traverse nums2 once to find the common elements.

# Space Complexity: O(n)
# - Dictionary stores the frequency of elements from nums1.
        