# LEETCODE 79: Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # Total number of rows and columns in the board
        rows = len(board)
        cols = len(board[0])

        # DFS function to search for the word
        # r = current row
        # c = current column
        # index = current character of the word we are looking for
        def dfs(r, c, index):

            # Base Case:
            # If index reaches the length of the word,
            # it means we have matched the required character
            if index == len(word):
                return True
            
            # Invalid Case:
            # 1. Current cell is outside the board
            # 2. Current cell does not match the required character
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[index]):
                return False

            # Save the current character before changing it
            temp = board[r][c]

            # Mark the current cell as visited
            # so that we don't use the same cell again
            board[r][c] = "#"

            # Explore all four possible direction
            # If any one of them finds the complete word,
            # 'found' becomes True
            found = (
                dfs(r + 1, c, index + 1) or #Down
                dfs(r - 1, c, index + 1) or #Up
                dfs(r, c + 1, index + 1) or #Right
                dfs(r, c - 1, index + 1)    #Left
            )

            # Backtracking Step:
            # Restore the original character because
            # another path may need to use this cell
            board[r][c] = temp

            # Return whether the word was found or not
            return found

        # Try starting the search from every cell of the board
        for r in range(rows):
            for c in range(cols):

                # Start searchinng from the first character of the word
                if dfs(r, c, 0):
                    return True

        # If no starting position works,
        # the word does not exist in the board
        return False
    
# Time Complexity: O(rows × cols × 4^L)
# - Start DFS from every cell.
# - At each step, explore up to 4 directions.
# - L = Length of the word.

# Space Complexity: O(L)
# - Recursion stack can grow up to the length of the word.