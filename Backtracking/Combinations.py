# LEETCODE 77: Combinations

# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# Example 1:

# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
# Example 2:

# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        # Store all possible combinations
        result = []

        # Store the current combination
        combination = []

        def backtrack(start):

            # If the current combination contains k numbers,
            # store it as one possible answer
            if len(combination) == k:
                result.append(combination[:])
                return

            # Try every possible number starting from 'start'
            for i in range(start, n + 1):

                # Choose the current number
                combination.append(i)

                # Explore further combinations
                backtrack(i + 1)

                # Backtrack by removing the last chosen number
                combination.pop()

        # Start choosing numbers from 1
        backtrack(1)

        # Return all possible combinations
        return result


# Time Complexity: O(C(n, k) × k)
# - There are C(n, k) valid combinations.
# - Copying each combination takes O(k).

# Space Complexity: O(k)
# - The recursion stack and current combination store at most k elements.
# - (Excluding the output array.)