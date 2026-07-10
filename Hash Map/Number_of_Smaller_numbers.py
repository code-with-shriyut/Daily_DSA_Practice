# LEETCODE 1365: How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
# That is, for each nums[i] you have to count the number of valid j's such that j != i 
# and nums[j] < nums[i].

# Return the answer in an array.
# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation: 
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1). 
# For nums[3]=2 there exist one smaller number than it (1). 
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
# Example 2:

# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# Example 3:

# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Create a sorted copy of the original array
        sorted_nums = sorted(nums)

        # Store each number and the count of numbers smaller than it
        smaller = {}

        # Traverse the sorted array
        for i in range(len(sorted_nums)):

            # Store only the first occurrence of each number
            if sorted_nums[i] not in smaller:
                smaller[sorted_nums[i]] = i

        # Store the final answer
        result = []

        # Find the answer for every number in the original array
        for num in nums:
            result.append(smaller[num])

        # Return the result
        return result


# Time Complexity: O(n log n)
# - Sorting the array takes O(n log n).
# - Traversing the sorted array takes O(n).
# - Traversing the original array takes O(n).

# Space Complexity: O(n)
# - Dictionary stores the first occurrence of each number.
# - The result array also uses O(n) space.