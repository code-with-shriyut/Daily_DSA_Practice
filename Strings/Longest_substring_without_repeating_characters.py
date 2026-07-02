# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Store the unique characters present in the current window
        charSet = set()

        # Left pointer of the sliding window
        l = 0

        # Store the length of the longest valid substring
        res = 0

        # Expand the window by moving the right pointer
        for r in range(len(s)):

            # If the current character is already in the window,
            # shrink the window until it becomes unique again
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            # Add the current character to the window
            charSet.add(s[r])

            # Update the maximum length found so far
            res = max(res, r - l + 1)

        # Return the length of the longest substring
        return res


# Time Complexity: O(n)
# - Each character is added to and removed from the set at most once.

# Space Complexity: O(min(n, m))
# - Stores unique characters in the current window.
# - n = length of the string
# - m = total number of unique characters