# Leetcode 1346
# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]

# Example 1:
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# Example 2:
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.
class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        seen = set()        # Create a set to store visited numbers
        for i in arr:        # Traverse each number in the array
            if i * 2 in seen or (i % 2 == 0 and i // 2 in seen): # Check if double of current number or half of current number already exists
              return True
            seen.add(i) # Add current number after checking to avoid using the same element twice
            return False         # No number and its double found

# Time Complexity in this case is O(n) since we are traversing the array once.
# Space Complexity in this case is O(n) since we are using Hashset to stored all visited elements from the array.