# Leetcode 40: Combination Sum II

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.

# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
 

# Constraints:

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        # Sort the array so that duplicate numbers come together
        candidates.sort()

        # Store all valid combinations
        result = []

        # Store the current combination
        combination = []

        def backtrack(index, current_sum):

            # If the target is reached, save the current combination
            if current_sum == target:
                result.append(combination[:])
                return

            # Stop if the current sum becomes greater than the target
            if current_sum > target:
                return

            # Try every element starting from the current index
            for i in range(index, len(candidates)):

                # Skip duplicate elements at the same recursion level
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # Choose the current element
                combination.append(candidates[i])

                # Move to the next index since each element can be used only once
                backtrack(i + 1, current_sum + candidates[i])

                # Remove the last element to try another combination
                combination.pop()

        # Start backtracking from index 0 with sum = 0
        backtrack(0, 0)

        # Return all valid combinations
        return result


# Time Complexity: O(2^n × n)
# - In the worst case, all possible combinations are explored.
# - Copying each valid combination takes O(n).

# Space Complexity: O(n)
# - Recursion stack and current combination can grow up to n elements.