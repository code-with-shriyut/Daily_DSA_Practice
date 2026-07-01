# LeetCode 520: Detect Capital
# We define the usage of capitals in a word to be right when one of the following cases holds:
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # Counts the number of uppercase letters in the word
        u_count = 0

        # Traverse each character and check if it is uppercase
        for ch in word:
            if 'A' <= ch <= 'Z':
                u_count += 1

        # Case 1:
        # If there are no uppercase letters,
        # the word is completely lowercase (e.g., "leetcode")
        if u_count == 0:
            return True

        # Case 2:
        # If every character is uppercase,
        # the word is completely uppercase (e.g., "USA")
        if u_count == len(word):
            return True

        # Case 3:
        # If there is exactly one uppercase letter
        # and it is the first character,
        # the word follows title case (e.g., "Google")
        if u_count == 1 and 'A' <= word[0] <= 'Z':
            return True

        # If none of the above cases match,
        # the capitalization is incorrect
        return False
    
"""
Time Complexity: O(n)
- Traverse the string once to count uppercase letters.

Space Complexity: O(1)
- Uses only a few variables regardless of the input size.
"""