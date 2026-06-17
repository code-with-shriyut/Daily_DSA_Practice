# LEETCODE 1480 : Running Sum of 1d Array

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        running_sum = [] #Initializing an empty list to store the running sum of the elements in the input list.
        total = 0 # Initializing a variable to keep track of the running total of the elements in the input list.

        for i in range(len(nums)):
            total += nums[i]
            running_sum.append(total) # Appending the running total to the running_sum list after each iteration of the loop.
        return running_sum
    

nums = [1, 2, 3, 4]
print(Solution().runningSum(nums))

# Time complexity in this case is O(n) because we are traversing the array once.
# Space complexity in this case is O(n) because we are using an extra array to store the desired output.