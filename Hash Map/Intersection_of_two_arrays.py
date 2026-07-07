# LEETCODE 349: Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

# ########## OPTIMAL APPROACH #########

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Store all unique elements of nums1
        seen = set(nums1)

        # Store the common elements
        result = set()

        # Check every element of nums2
        for num in nums2:

            # If the element is present in nums1
            if num in seen:
                result.add(num)

        # Return the common elements as a list
        return list(result)


# Time Complexity: O(n + m)
# - Creating the set takes O(n).
# - Traversing nums2 takes O(m).

# Space Complexity: O(n)
# - Extra space is used for the sets.


######### BRUTE FORCE APPROACH #########
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """

#         # Store the common unique elements
#         s = set()

#         # Traverse every element of nums1
#         for num in nums1:

#             # Compare it with every element of nums2
#             for i in range(len(nums2)):

#                 # If both elements are equal and not already added
#                 if nums2[i] == num and nums2[i] not in s:

#                     # Store the common element
#                     s.add(nums2[i])

#         # Convert the set into a list and return it
#         return list(s)


# Time Complexity: O(n × m)
# - For every element in nums1, we compare it with every element in nums2.

# Space Complexity: O(min(n, m))
# - The set stores only the unique common elements.