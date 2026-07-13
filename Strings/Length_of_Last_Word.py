# LEETCODE 58: Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Start from the last character of the string

        i = len(s) - 1

        # Skip all trailing Spaces
        while i >= 0 and s[i] == " ":
            i -= 1
        
        # Store the length of the last word
        count = 0

        # Count the characters of the last word
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1
        
        #Return the length of the last word
        return count

# Time Complexity: O(n)
# - In the worst case, we traverse the string once.

# Space Complexity: O(1)
# - No extra data structure is used.