# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

# Example 2:
# Input: nums = [0]
# Output: [[],[0]]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Sort the array so that duplicate numbers come together.
        # This makes it easy to skip repeated subsets.
        nums.sort()

        # Store all unique subsets.
        result = []

        # Store the current subset being built.
        subset = []

        def backtrack(index):

            # Every subset formed so far is a valid answer,
            # so save a copy of it.
            result.append(subset[:])

            # Try every possible element starting from the current index.
            for i in range(index, len(nums)):

                # If the current element is the same as the previous one
                # at the same recursion level, skip it.
                # Otherwise, we would generate duplicate subsets.
                if i > index and nums[i] == nums[i - 1]:
                    continue

                # Choose the current element.
                subset.append(nums[i])

                # Continue building the subset using the remaining elements.
                backtrack(i + 1)

                # Remove the last element so that we can
                # try another possible subset.
                subset.pop()

        # Start generating subsets from index 0.
        backtrack(0)

        # Return all unique subsets.
        return result


# Time Complexity: O(n × 2^n)
# - There can be up to 2^n unique subsets.
# - Copying each subset into the result takes O(n).

# Space Complexity: O(n)
# - The recursion stack and the current subset
#   can grow up to n elements.