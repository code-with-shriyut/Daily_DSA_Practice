# LEETCODE 52: N-Queens II

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
# such that no two queens attack each other.
# Given an integer n, return the number of distinct solutions to the n-queens puzzle.

# Example 1:

# Input: n = 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
# Example 2:

# Input: n = 1
# Output: 1

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """

        # Store occupied columns
        columns = set()

        # Store occupied main diagonals (\)
        diagonal1 = set()

        # Store occupied anti-diagonals (/)
        diagonal2 = set()

        def backtrack(row):

            # If queens are successfully placed in all rows,
            # we found one valid solution
            if row == n:
                return 1

            # Store the number of valid solutions
            count = 0

            # Try placing the queen in every column
            for col in range(n):

                # Skip unsafe positions
                if (col in columns or
                    (row - col) in diagonal1 or
                    (row + col) in diagonal2):
                    continue

                # Place the queen
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                # Count all solutions from the next row
                count += backtrack(row + 1)

                # Undo the previous choice
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

            # Return the total solutions found from this row
            return count

        # Start from the first row
        return backtrack(0)


# Time Complexity: O(N!)
# Space Complexity: O(N)