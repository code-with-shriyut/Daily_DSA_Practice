# LEETCODE 242: Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # Store the frequency of each character in string 's'
        frequency_s = {}

        # Store the frequency of each character in string 't'
        frequency_t = {}

        # Count the frequency of every character in 's'
        for char in s:
            if char in frequency_s:
                frequency_s[char] += 1
            else:
                frequency_s[char] = 1

        # Count the frequency of every character in 't'
        for char in t:
            if char in frequency_t:
                frequency_t[char] += 1
            else:
                frequency_t[char] = 1

        # If both frequency dictionaries are the same,
        # the two strings are anagrams
        if frequency_s == frequency_t:
            return True

        # Otherwise, they are not anagrams
        return False


# Time Complexity: O(n + m)
# - Traverse both strings once to count the frequency of characters.
# - Comparing the two dictionaries also takes linear time.

# Space Complexity: O(n + m)
# - Two dictionaries are used to store the character frequencies.