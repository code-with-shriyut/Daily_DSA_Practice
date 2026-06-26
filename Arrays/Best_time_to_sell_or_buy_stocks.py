# Leetcode 121

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        # Assume the first day's price is the minimum buying price
        min_price = prices[0]

        # Initially, no profit is made
        max_profit = 0


        # Traverse the price list from the second day
        for i in range(1, len(prices)):

            # Update the minimum buying price if a lower price is found
            min_price = min(min_price, prices[i])

            # Calculate profit if sold on the current day
            current_profit = prices[i] - min_price

            # Update the maximum profit
            max_profit = max(max_profit, current_profit)


        # Return the maximum profit
        return max_profit


# Time Complexity: O(n)
# - Traverse the prices array only once.

# Space Complexity: O(1)
# - Only constant extra variables are used.