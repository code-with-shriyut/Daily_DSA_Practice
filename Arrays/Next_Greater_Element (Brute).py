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

        result = []

        # Traverse every element of nums1
        for num in nums1:

            found = False

            # Find the element in nums2
            for i in range(len(nums2)):

                if nums2[i] == num:

                    # Search towards the right
                    for j in range(i + 1, len(nums2)):

                        if nums2[j] > num:

                            result.append(nums2[j])
                            found = True
                            break

                    # Stop because the element has been found
                    break

            # No greater element exists
            if not found:
                result.append(-1)

        return result
    
# Time Complexity: O(m × n)
# - For each element in nums1, we may scan nums2 to find it,
#   and then scan the remaining part of nums2 to find the next greater element.

# Space Complexity: O(1)
# - Only the output list is used (excluding the returned answer).