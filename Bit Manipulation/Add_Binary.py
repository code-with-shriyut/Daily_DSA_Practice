# LEETCODE 67: Add Binary
# Given two binary strings a and b, return their sum as a binary string.
# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Start from the last character of both binary strings
        i = len(a) - 1
        j = len(b) - 1

        # Store the carry generated during addition
        carry = 0
        
        # Store the final binary result
        result = []
        
        # Continue until all digits are processed or there's no carry left
        while i >= 0 or j >= 0 or carry:
            
            # Start with the carry from the previous addition
            total = carry

            # Add the current digit from string 'a'
            if i >= 0:
                total += int(a[i])
                i -= 1
            
            # Add the current digit from string 'b'
            if j >= 0:
                total += int(b[j])
                j -= 1

            # Store the current binary digit

            result.append(str(total % 2))

            # Calculate the carry for the next iteration
            carry = total // 2

        # Reverse the result because it was built from right to left
        return "".join(result[::-1])

# Time Complexity: O(max(n, m))
# - Traverse both binary strings once.

# Space Complexity: O(max(n, m))
# - Store the resulting binary number.

