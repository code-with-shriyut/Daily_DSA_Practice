# LEETCODE 229: Majority Element II

# Given an integer array of size n, find all elements that appear more than ⌊n / 3⌋ times.

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]

# APPROACH : Boyre-Moore Voting Algorithm

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # Store the two possible majority candidates
        candidate1 = None
        candidate2 = None

        # Store their vote counts
        count1 = 0
        count2 = 0

        # ---------- First Pass ----------
        # Find the two possible majority candidates
        for num in nums:

            # If the current number matches candidate1,
            # increase its count
            if candidate1 == num:
                count1 += 1

            # If the current number matches candidate2,
            # increase its count
            elif candidate2 == num:
                count2 += 1

            # If candidate1 has no votes left,
            # choose the current number as candidate1
            elif count1 == 0:
                candidate1 = num
                count1 = 1

            # If candidate2 has no votes left,
            # choose the current number as candidate2
            elif count2 == 0:
                candidate2 = num
                count2 = 1

            # Otherwise, cancel one vote from both candidates
            else:
                count1 -= 1
                count2 -= 1

        # ---------- Second Pass ----------
        # Count the actual frequency of both candidates
        count1 = 0
        count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1

        # Store the final answer
        result = []

        # Check if candidate1 appears more than n//3 times
        if count1 > len(nums) // 3:
            result.append(candidate1)

        # Check if candidate2 appears more than n//3 times
        if count2 > len(nums) // 3:
            result.append(candidate2)

        # Return all majority elements
        return result


# Time Complexity: O(n)
# - First pass finds the possible candidates.
# - Second pass verifies their frequencies.

# Space Complexity: O(1)
# - Only a few variables are used.