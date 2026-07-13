# LEETCODE 51: N-Queens

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # Store all valid solutions
        result = []

        # Create an empty n x n chess board
        board = [["." for _ in range(n)] for _ in range(n)]

        # Store the columns where a queen is already placed
        columns = set()

        # Store the occupied main diagonals (\)
        # Main diagonal is identified by (row - col)
        diagonal1 = set()

        # Store the occupied anti-diagonals (/)
        # Anti-diagonal is identified by (row + col)
        diagonal2 = set()

        def backtrack(row):

            # If we successfully placed queens in all rows,
            # save the current board as one valid solution
            if row == n:
                result.append(["".join(r) for r in board])
                return

            # Try placing the queen in every column of the current row
            for col in range(n):

                # If this position is already under attack,
                # skip it and try the next column
                if (col in columns or
                    (row - col) in diagonal1 or
                    (row + col) in diagonal2):
                    continue

                # Place the queen on the board
                board[row][col] = "Q"

                # Mark this column and both diagonals as occupied
                columns.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col)

                # Try placing the queen in the next row
                backtrack(row + 1)

                # Backtracking:
                # Remove the queen because now we want to
                # try another column in the same row
                board[row][col] = "."

                # Remove the occupied marks so that
                # future choices can use them again
                columns.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)

        # Start placing queens from the first row
        backtrack(0)

        # Return all valid chess boards
        return result


# Time Complexity: O(N!)
# - In the worst case, we try many different queen placements.

# Space Complexity: O(N)
# - Used by the recursion stack and the three sets.
# - (Output space is not included.)