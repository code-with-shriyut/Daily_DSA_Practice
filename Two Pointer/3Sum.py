# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        # Stores all unique triplets
        result = []

        # Fix one element at a time
        for i in range(len(nums) - 2):

            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i -1]:
                continue

            # Start two pointers
            left = i + 1
            right = len(nums) - 1

            # Search for the other two numbers
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                # If the sum is 0, a valid triplets is found:
                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates values for the left pointer

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    # Skip duplicates values for the right pointer
                    
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers to search for a new pair
                    left += 1
                    right -= 1
                
                # If the sum is too small, move the left pointer
                elif total < 0:
                    left += 1
                 # If the sum is too large, move the right pointer

                else:
                    right -= 1
        # Return all unique triplets            
        return result
    
# Time Complexity: O(n²)
# - Sorting takes O(n log n).
# - For each fixed element, the two pointers scan the remaining array once.

# Space Complexity: O(1)
# - Only constant extra space is used (excluding the output list).