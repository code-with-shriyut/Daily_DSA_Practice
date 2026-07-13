# LEETCODE 387: First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"

# Output: 0

# Explanation:

# The character 'l' at index 0 is the first character that does not occur at any other index.

# Example 2:

# Input: s = "loveleetcode"

# Output: 2

# Example 3:

# Input: s = "aabb"

# Output: -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Store the frequency of each character
        frequency = {}

        # Count how many times each character appears
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

        # Traverse the string again
        for i in range(len(s)):

            # If the current character appears only once,
            # return its index
            if frequency[s[i]] == 1:
                return i

        # No unique character found
        return -1


# Time Complexity: O(n)
# - First traversal counts the frequency of each character.
# - Second traversal finds the first unique character.

# Space Complexity: O(1)
# - At most 26 lowercase English letters are stored in the hashmap.
# - (Generally considered O(1) for this problem.)