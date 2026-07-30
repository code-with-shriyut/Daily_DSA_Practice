# LEETCODE 904: Fruit Into Baskets
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].

from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # Left boundary of the sliding window
        left = 0

        # Stores the maximum number of fruits collected
        maxLength = 0

        # Stores the frequency of each fruit type in the current window
        basket = defaultdict(int)

        # Expand the window by moving the right pointer
        for right in range(len(fruits)):

            # Add the current fruit to the basket
            basket[fruits[right]] += 1

            # Shrink the window until it contains at most 2 fruit types
            while len(basket) > 2:

                # Remove the leftmost fruit from the basket
                basket[fruits[left]] -= 1

                # Remove the fruit type if its count becomes zero
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                # Move the left boundary forward
                left += 1

            # Update the maximum valid window size
            maxLength = max(maxLength, right - left + 1)

        # Return the maximum fruits collected
        return maxLength

# Time Complexity: O(n)
# - Each fruit enters and leaves the window at most once.

# Space Complexity: O(1)
# - The basket stores at most 2 fruit types
#   (temporarily 3 before shrinking).

# Approach:
#
# Use the Sliding Window technique.
#
# Maintain a window containing at most
# two distinct fruit types.
#
# - Expand the window by moving the
#   right pointer and add the current fruit.
#
# - If the window contains more than
#   two fruit types, shrink it from
#   the left until it becomes valid.
#
# - Update the maximum window size
#   after every valid window.