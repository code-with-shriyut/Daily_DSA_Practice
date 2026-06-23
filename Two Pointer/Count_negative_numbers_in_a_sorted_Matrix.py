# Leetcode 1351
# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.

# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0
class Solution(object):
    def countNegatives(self, grid):

        rows = len(grid) # Get total number of rows in matrix
        cols = len(grid[0])  # Get total number of columns in matrix
        r = 0  # Start from the first row
        c = cols - 1  # Start from the last column (top-right corner)
        count = 0  # Store total negative numbers
        while r < rows and c >= 0: # Traverse matrix until row or column goes out of range
            if grid[r][c] < 0: # If current element is negative
                # All elements below current element are also negative
                # Add all those negatives at once
                count += rows - r
                c -= 1  # Move left to check previous column
            else:
                # Current value is positive,
                # move down to find smaller values
                r += 1
        return count # Return total count of negative numbers

# Time Complexity: O(m + n)
# - Each step eliminates either one row or one column.
# - We traverse at most m rows and n columns.

# Space Complexity: O(1)
# - The counting is done in-place.
# - No additional memory is used apart from a few variables.