# LEETCODE 496: Next Greater Element I 
# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:

# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# Example 2:

# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Stack to store elements whose next greater element
        # has not been found yet
        stack = []

        # Dictionary to store the next greater element
        # for every value in nums2
        next_greater = {}

        # Traverse nums2
        for num in nums2:

            # If the current number is greater than the top of the stack,
            # then it is the next greater element for the top value
            while stack and num > stack[-1]:

                # Remove the top element from the stack
                top = stack.pop()

                # Store its next greater element
                next_greater[top] = num

            # Current element is still waiting for its
            # next greater element, so push it into the stack
            stack.append(num)

        # The remaining elements in the stack
        # do not have any greater element on their right
        while stack:

            # Remove the remaining element
            top = stack.pop()

            # Store -1 because no greater element exists
            next_greater[top] = -1

        # Build the final answer for nums1
        result = []

        for num in nums1:

            # Get the next greater element from the dictionary
            result.append(next_greater[num])

        # Return the final result
        return result


# Time Complexity: O(n + m)
# - Traverse nums2 once to build the dictionary.
# - Traverse nums1 once to build the final answer.

# Space Complexity: O(n)
# - Stack and dictionary store elements from nums2.