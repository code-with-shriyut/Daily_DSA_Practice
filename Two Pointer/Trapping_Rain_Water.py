# LEETCODE 42: Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it can trap after raining.

# Example 1:

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 
# Constraints:
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5

#------------------------------Two Pointer Approach------------------------------#
class Solution:
    def trap(self, height: List[int]):

        # Initialize two pointers at both ends of the array
        left = 0
        right = len(height) - 1

        # Store the maximum height seen so far from both sides
        leftMax = 0
        rightMax = 0

        # Stores the total trapped water
        water = 0

        # Continue until both pointers meet
        while left < right:

            # Update the maximum height from both directions
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            # Process the side with the smaller maximum height
            if leftMax < rightMax:

                # Water trapped at the current left position
                water += leftMax - height[left]

                # Move the left pointer forward
                left += 1

            else:

                # Water trapped at the current right position
                water += rightMax - height[right]

                # Move the right pointer backward
                right -= 1

        # Return the total trapped water
        return water

# Time Complexity: O(n)
# - Each pointer moves towards the center only once.
# - Every element is processed at most one time.

# Space Complexity: O(1)
# - Only a few variables and two pointers are used.
# - No extra array is required.

# Approach:
#
# Use two pointers, one at the beginning and one at the end.
#
# Keep track of the maximum height seen from the left
# and the maximum height seen from the right.
#
# The side with the smaller maximum height determines
# how much water can be trapped.
#
# - If leftMax < rightMax:
#     Water trapped = leftMax - current height.
#     Move the left pointer.
#
# - Otherwise:
#     Water trapped = rightMax - current height.
#     Move the right pointer.
#
# Continue until both pointers meet.

#------------------------Prefix and Suffix Arrays Approach---------------------------#

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)

#         # Edge case: Less than 3 bars cannot trap water
#         if n < 3:
#             return 0

#         # Step 1: Build LeftMax array
#         leftMax = [0] * n
#         leftMax[0] = height[0]

#         for i in range(1, n):
#             leftMax[i] = max(leftMax[i - 1], height[i])

#         # Step 2: Build RightMax array
#         rightMax = [0] * n
#         rightMax[-1] = height[-1]

#         for i in range(n - 2, -1, -1):
#             rightMax[i] = max(rightMax[i + 1], height[i])

#         # Step 3: Calculate trapped water
#         totalWater = 0

#         for i in range(n):
#             water = min(leftMax[i], rightMax[i]) - height[i]
#             totalWater += water

#         return totalWater

# Time Complexity: O(n)
# - One pass to build LeftMax.
# - One pass to build RightMax.
# - One pass to calculate trapped water.
# - Overall: O(n)

# Space Complexity: O(n)
# - Two extra arrays (LeftMax and RightMax)
#   of size n are used.

# Approach:
#
# Water trapped at any index depends on:
#
#     min(Max height on the left,
#         Max height on the right)
#     - Current bar height
#
# Step 1:
# Build a LeftMax array where each index stores
# the tallest bar seen from the left.
#
# Step 2:
# Build a RightMax array where each index stores
# the tallest bar seen from the right.
#
# Step 3:
# For every index, calculate:
#
#     Water = min(leftMax, rightMax) - height
#
# Add the water trapped at each index to get
# the total trapped water.