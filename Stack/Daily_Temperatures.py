# LEETCODE 739: Daily Temperatures

# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # Store the answer for each day
        result = [0] * len(temperatures)

        # Stack stores the indices of temperatures
        stack = []

        # Traverse all temperatures
        for i in range(len(temperatures)):

            # While the current temperature is warmer than
            # the temperature at the index on the top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:

                # Get the index of the previous colder day
                previous_index = stack.pop()

                # Calculate the number of days to wait
                result[previous_index] = i - previous_index

            # Push the current index onto the stack
            stack.append(i)

        # Return the final answer
        return result


# Time Complexity: O(n)
# - Every index is pushed onto the stack once.
# - Every index is popped from the stack once.

# Space Complexity: O(n)
# - Stack may store up to n indices.
# - Result array also uses O(n) space.