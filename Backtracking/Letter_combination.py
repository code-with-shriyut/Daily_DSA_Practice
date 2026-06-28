# Leetcode 17: Letter Combination of a Phone number.

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:

# Input: digits = "2"
# Output: ["a","b","c"]

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # If the input is empty, no combinations can be formed.
        if not digits:
            return []
        # Mapping of digits to their corresponding letters
        phone = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        # Store all possible letter combinations
        result = []

        def backtrack(index, current):

            # If all digits have been processed, one complete combination is ready.
            if index == len(digits):
                result.append(current)
                return
            # Get all letters for the current digit
            letters = phone[digits[index]]
            
            # Try every letter one by one
            for ch in letters:
                # Add the current letter and move to the next digit
                backtrack(index + 1, current + ch)

        # Start from the first digit with an empty string
        backtrack(0, "")
        # Return all possible combinations
        return result

# Time Complexity: O(4^n × n)
# Space Complexity: O(n)
