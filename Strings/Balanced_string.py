# Leetcode 3340: Check Balanced String

# You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.
# Return true if num is balanced, otherwise return false.

# Example 1:
# Input: num = "1234"
# Output: false
# Explanation:
# The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
# Since 4 is not equal to 6, num is not balanced.

# Example 2:
# Input: num = "24123"
# Output: true
# Explanation:
# The sum of digits at even indices is 2 + 1 + 3 == 6, and the sum of digits at odd indices is 4 + 2 == 6.
# Since both are equal the num is balanced.

class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """

        # Store the sum of digits at even indices
        even = 0

        # Store the sum of digits at odd indices
        odd = 0


        # Traverse each digit of the string
        for i in range(len(num)):

            # Add digit if the index is even
            if i % 2 == 0:
                even += int(num[i])

            # Otherwise, add digit to the odd sum
            else:
                odd += int(num[i])


        # Return True if both sums are equal, otherwise False
        return even == odd


# Time Complexity: O(n)
# - Traverse the string once and process each digit exactly one time.

# Space Complexity: O(1)
# - Only two variables (even and odd) are used.