# LEETCODE 12: Integer to Roman

# Approach: Greedy Algorithm
#
# Always choose the largest Roman numeral value that is less than or equal
# to the remaining number. Add its Roman symbol to the answer and subtract
# its value from the number. Repeat this process until the number becomes 0.
#
# Since the Roman values are stored in descending order (including special
# cases like 900 = CM, 90 = XC, 4 = IV), this greedy approach always
# produces the correct Roman numeral.

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # Roman numeral values arranged from largest to smallest.
        values = [1000, 900, 500, 400,
                  100, 90, 50, 40,
                  10, 9, 5, 4, 1]

        # Roman symbols corresponding to each value.
        romans = ["M", "CM", "D", "CD",
                  "C", "XC", "L", "XL",
                  "X", "IX", "V", "IV", "I"]

        # Stores the final Roman numeral.
        result = ""

        # Traverse each Roman value from largest to smallest.
        for i in range(len(values)):

            # If the current Roman value can fit into the remaining number,
            # keep using it until it no longer fits.
            # Each time:
            #   1. Add its Roman symbol to the answer.
            #   2. Subtract its value from the number.
            while num >= values[i]:
                result += romans[i]
                num -= values[i]

        # Return the complete Roman numeral.
        return result
    
# Time Complexity: O(1) - The algorithm runs in constant time since the number of Roman numeral symbols is fixed 
# and does not depend on the input size.

# Space Complexity: O(1) - The space used for the result string is proportional 
# to the number of symbols in the Roman numeral representation, which is bounded by a constant for any valid input integer.