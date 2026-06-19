# Example 1:
# Input: nums = [1,1,2,3,3]
# Output: [1,2,3]

# Example 2:
# Input: nums = [0,0,1,1,2,2,3,3,4,4]
# Output: [0,1,2,3,4]

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # If the array is empty, there are no unique elements.
        if not nums:
            return 0
        # Pointer to track the positio of the next unique element.
        j = 0 
        for i in range(1, len(nums)): #Traverse the array starting from index 1.
            # check if a new element is found.
            if nums[i] != nums[j]: 
                # Update position for unique element.
                j += 1 
                # Replacing duplicate position with unique elements
                nums[j] = nums[i] 
        # Returns the array containing only unique values.
        return nums[:j+1]   

nums = [0,0,1,1,1,2,2,3,3,3,4]
print(Solution().removeDuplicates(nums))

# Time complexity in this case is O(n), beacause the pointer i iterates for n number of times.
# Space complexity in this case is O(1), beacause no extra space is used.
