# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.
# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

# Example 1:
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.

# Example 2:
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.

# Example 3:
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        start = 0
        end = len(letters) - 1
        ans = letters[0]
        while start <= end:
            mid = start + (end - start) // 2
            if letters[mid] > target:
                ans = letters[mid]   # Current letter is greater than target. It can be a possible answer
                end = mid - 1   # Search for smaller valid letter
            else:
                start = mid + 1  # Current letter is too small
        return ans


# Time Complexity: O(log n)
# - Binary search reduces the search space by half in every iteration.

# Space Complexity: O(1)
# - No extra data structure is used.