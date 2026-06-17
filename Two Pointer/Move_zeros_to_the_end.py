
# LEETCODE 283 : Move Zeros
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

arr = [1, 0, 2, 0, 3, 0, 4]
j = 0     # j is the pointer that will keep track of the position of the next non-zero element.
for i in range(len(arr)):
    if arr[i] != 0:
        arr[j], arr[i] = arr[i], arr[j] # Swapping the non-zero element with the element at index j.
        j += 1

print(arr)

# Time complexity in this case is O(n) becuase we are traversing the array once.
# Space complexity in this case is O(1) since we are not using any extra array.