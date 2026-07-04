# LEETCODE 11: Container with Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        # A variable to store the maximum area of water 
        # that can be contained between two lines.
        res = 0 

        left = 0 
        right = n - 1

        # Continue the loop until the two pointers meet.
        while left < right:

            # The area of water that can be contained between the two lines 
            # is calculated by taking the minimum of the two heights 
            # and multiplying it by the distance between them (right - left). 
            water = min(height[left], height[right]) * (right - left)

            # Update the maximum area if the current area is greater than the previous maximum.
            res = max(water, res)

            # Move the pointer with the smaller height
            # because moving the taller one cannot increase the area
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
                
        # Return the maximum water area        
        return res

# Time Complexity: O(n)
# - Both pointers move towards each other only once.
# - Each element is visited at most one time.

# Space Complexity: O(1)
# - Only a few variables are used.
# - No extra data structure is required.