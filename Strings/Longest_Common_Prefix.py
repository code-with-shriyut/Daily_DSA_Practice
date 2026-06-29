# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

 
# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Take the first string as reference
        first = strs[0]

        # Check every character of the first string
        for i in range(len(first)):

            # Compare with all other strings
            for word in strs[1:]:

                # Character doesn't exist or doesn't match
                if i == len(word) or word[i] != first[i]:
                    return first[:i]

        # Entire first string is the common prefix
        return first
    
# Time Complexity: O(n × m)

# Space Complexity: O(1)
