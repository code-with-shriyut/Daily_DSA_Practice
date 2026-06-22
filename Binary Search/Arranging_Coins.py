# You have n coins and you want to build a staircase with these coins. 
# The staircase consists of k rows where the ith row has exactly i coins. 
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

 

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        answer = 0
        while left <= right:
            mid = left + (right - left) // 2 # Possible number of rows == mid can be made.
            coins = mid * (mid + 1) // 2 # Calculate the number of coins need to make 'mid' number of rows(1+2+3+4+5+....+mid).        
            if coins <= n: # If required coins are within available number of coins, these rows can be formed.
                answer = mid
                left = mid + 1 # Try to make more rows if any coins are left.
            else:
                right = mid - 1 # If too many coins are needed, try to make fewer rows.
        return answer

# Time Complexity in this case is O(log n) since Binary search is applied on possible number of rows.
# Space Complexity in this case is O(1) since no extra data structure is used.