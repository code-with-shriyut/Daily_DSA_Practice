# Leetcode Problem: 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        # Check every possible starting position
        for i in range(len(haystack) - len(needle) + 1):

            j = 0

            # Compare characters one by one
            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1

            # If all characters matched
            if j == len(needle):
                return i

        # Needle not found
        return -1


# Time Complexity: O((n - m + 1) × m)
# - n = Length of haystack
# - m = Length of needle
# - In the worst case, every starting position is checked.

# Space Complexity: O(1)
# - No extra space is used.