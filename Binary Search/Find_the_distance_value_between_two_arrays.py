# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

# Example 1:
# Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
# Output: 2
# Explanation: 
# For arr1[0]=4 we have: 
# |4-10|=6 > d=2 
# |4-9|=5 > d=2 
# |4-1|=3 > d=2 
# |4-8|=4 > d=2 
# For arr1[1]=5 we have: 
# |5-10|=5 > d=2 
# |5-9|=4 > d=2 
# |5-1|=4 > d=2 
# |5-8|=3 > d=2
# For arr1[2]=8 we have:
# |8-10|=2 <= d=2
# |8-9|=1 <= d=2
# |8-1|=7 > d=2
# |8-8|=0 <= d=2

# Example 2:
# Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
# Output: 2

# Example 3:
# Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
# Output: 1
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):

        # Sort arr2 so that we can search faster using binary search
        arr2.sort()


        # Count elements of arr1 which satisfy the condition
        count = 0


        # Pick each number from arr1 one by one
        for x in arr1:


            # Starting and ending position of arr2
            left = 0
            right = len(arr2) - 1


            # Assume x has no close value in arr2
            valid = True


            while left <= right:


                # Find the middle element of arr2
                mid = left + (right - left) // 2


                # If any arr2 element is close to x,
                # x is not a valid answer
                if abs(x - arr2[mid]) <= d:

                    valid = False
                    break


                # Current arr2 value is smaller,
                # move towards bigger values
                elif arr2[mid] < x:

                    left = mid + 1


                # Current arr2 value is bigger,
                # move towards smaller values
                else:

                    right = mid - 1


            # If no close number was found in arr2,
            # include this element in answer
            if valid:

                count += 1
                
        return count
# Time Complexity: O(m log m + n log m) - Sorting + Binary search for each arr1 element
# Space Complexity: O(1) - Constant extra space