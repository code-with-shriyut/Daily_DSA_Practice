# LEETCODE 5: Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str):

        # Expands from the center and returns the longest palindrome
        def expand(left, right):

            # Keep expanding while characters match
            # and both pointers stay within the string
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Return the palindrome found
            return s[left + 1:right]

        # Stores the longest palindrome found so far
        longest = ""

        # Consider every index as the center of a palindrome
        for i in range(len(s)):

            # Check for an odd-length palindrome (e.g. "aba")
            odd = expand(i, i)

            # Check for an even-length palindrome (e.g. "abba")
            even = expand(i, i + 1)

            # Update the longest palindrome if needed
            if len(odd) > len(longest):
                longest = odd

            # Update the longest palindrome if needed
            if len(even) > len(longest):
                longest = even

        # Return the longest palindromic substring
        return longest

# Time Complexity: O(n²)
# - For every character, we may expand
#   up to the entire length of the string.

# Space Complexity: O(1)
# - Only a few variables are used.
# - No extra data structure is required.

# Approach:
#
# Every palindrome has a center.
#
# For each index in the string,
# treat it as the center and expand
# in both directions as long as the
# characters are equal.
#
# There are two possible centers:
#
# 1. Odd-length palindrome
#    Example: "aba"
#    Center = one character
#
# 2. Even-length palindrome
#    Example: "abba"
#    Center = between two characters
#
# Find the longest palindrome for
# both cases and keep updating the answer.