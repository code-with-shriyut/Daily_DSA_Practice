# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

nums = [1, 2, 3, 4, 8, 5, 7]
target = 12
seen = {} # We used a dictionary to store the values we have seen so far and their corresponding indices.
for i in range(len(nums)):
    value = nums[i]
    c = target - value # We are calculating the value we need to find in order to reach the target.
    if c in seen:
        print(seen[c], i) # If we found the value we need, we return the indices of both the required values that add up to the target.
    else:
        seen[value] = i # If we haven't found the value we need, we add the current value and its index to the dictionary.

# Time complexity in this case is O(n) because we are traversing the array once.
# Space complexity in this case is O(n) because we are using a dictionary to store the values we have seen and their corresponding indices.
