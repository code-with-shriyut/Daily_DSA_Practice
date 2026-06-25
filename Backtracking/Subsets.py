# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = [] # Stores all the generated subsets.
        subset = [] # Stores the subset we are currently building.


        def backtrack(index):

            # Base Condition:
            # If we checked all numbers,
            # store the current subset as one of the possible answer.
            if index == len(nums):
                result.append(subset[:])
                return


            # Choice 1: take element

            # Add current number into our subset.
            subset.append(nums[index])
            # Move to the next index and explore further choices.
            backtrack(index + 1)


            # Bactracking Step:
            # We are removing the number we added above so we can try another possibility.
            subset.pop()


            # Choice 2: skip element
            # Move forward without taking the current number
            backtrack(index + 1)

        # Start exploring choices from index 0
        backtrack(0)
        
        # Return all possible subsets
        return result
    
# Time Complexity O(2^n)
# Space Complexity O(n)