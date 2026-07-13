# LEETCODE 2423: Remove Letter To Equalize Frequency

# You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and 
# remove the letter at that index from word so that the frequency of every letter present in word is equal.
# Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

# Note:

# The frequency of a letter x is the number of times it occurs in the string.
# You must remove exactly one letter and cannot choose to do nothing.
 

# Example 1:

# Input: word = "abcc"
# Output: true
# Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
# Example 2:

# Input: word = "aazz"
# Output: false
# Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. 
# It is impossible to make all present letters have equal frequency.

class Solution(object):
    def equalFrequency(self, word):
        """
        :type word: str
        :rtype: bool
        """

        # Store the frequency of each character
        freq = {}

        # Count the frequency of every character
        for char in word:
            freq[char] = freq.get(char, 0) + 1

        # Try removing one occurrence of every character
        for char in freq:

            # Remove one occurrence
            freq[char] -= 1

            # Store all non-zero frequencies
            frequencies = set()

            for value in freq.values():
                if value > 0:
                    frequencies.add(value)

            # If all remaining frequencies are the same
            if len(frequencies) == 1:
                return True

            # Restore the removed occurrence
            freq[char] += 1

        # No valid removal found
        return False


# Time Complexity: O(n)
# - Counting frequencies takes O(n).
# - We try removing each distinct character (at most 26 lowercase letters).
# - Checking frequencies is also bounded by the alphabet size.

# Space Complexity: O(1)
# - At most 26 lowercase English letters are stored.