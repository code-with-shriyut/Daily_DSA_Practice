# LEETCODE 647: Palindromic Substrings

# Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


class Solution:
    def countSubstrings(self, s: str) -> int:

        # Expand around a center and count
        # all palindromes found from that center
        def expand(left, right):
            count = 0

            # Keep expanding while characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        # Stores the total number of palindromic substrings
        count = 0

        # Try every position as a possible center
        for i in range(len(s)):

            # Check odd-length palindromes
            # Example: "aba"
            odd = expand(i, i)

            # Check even-length palindromes
            # Example: "abba"
            even = expand(i, i + 1)

            # Add both types to the total count
            count += odd
            count += even

        return count

# Time Complexity: O(n²)
# - We try every index as a center.
# - From each center, we may expand up to O(n).

# Space Complexity: O(1)
# - Only a few variables are used.
# - No extra array or data structure is required.


# Approach:
#
# Every palindrome has a center.
#
# For each index, consider two possible centers:
#
# 1. (i, i)
#    → Odd-length palindrome
#    → Example: "aba"
#
# 2. (i, i + 1)
#    → Even-length palindrome
#    → Example: "abba"
#
# Expand outward while both characters are equal.
# Every successful expansion represents one palindrome.
#
# Add the count from every center to get the
# total number of palindromic substrings.