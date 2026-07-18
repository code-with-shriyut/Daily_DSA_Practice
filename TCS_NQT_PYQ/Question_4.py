## Closest Element Using Binary Search ##

# Problem Statement:
# Given a sorted array and a key, perform Binary Search.
# If the key is found, print the key.
# Otherwise, print the element whose value is closest (minimum absolute difference) to the key.
# If two elements are equally close, print the smaller element.

# Example 1

# Input:
# arr = [1, 3, 5, 7, 9]
# key = 6
# Output:
# 5

# Example 2

# Input:
# arr = [1, 3, 5, 7, 9]
# key = 7
# Output:
# 7

# Example 3

# Input:
# arr = [1, 3, 5, 7, 9]
# key = 8
# Output:
# 7

# SOLUTION:

# Input the size of the array
n = int(input())

# Input the sorted array
arr = list(map(int, input().split()))

# Input the key to search
key = int(input())

# Initialize the search boundaries
left = 0
right = n - 1

# Perform Binary Search
while left <= right:

    # Find the middle index
    mid = (left + right) // 2

    # If the key is found, print it and stop the program
    if arr[mid] == key:
        print(arr[mid])
        exit()

    # If the middle element is smaller than the key,
    # search in the right half
    elif arr[mid] < key:
        left = mid + 1

    # Otherwise, search in the left half
    else:
        right = mid - 1

# ------------------------------
# Key was NOT found in the array
# At this point:
# right -> largest element smaller than the key
# left  -> smallest element greater than the key
# ------------------------------

# If the key is greater than every element,
# the closest element is the last element
if left >= n:
    print(arr[right])

# If the key is smaller than every element,
# the closest element is the first element
elif right < 0:
    print(arr[left])

# Otherwise, compare both neighbouring elements
else:

    # Calculate the distance of both neighbours from the key
    diff1 = abs(arr[left] - key)
    diff2 = abs(arr[right] - key)

    # Print the element having the smaller difference
    if diff1 < diff2:
        print(arr[left])

    elif diff2 < diff1:
        print(arr[right])

    # If both are equally close,
    # print the smaller element
    else:
        print(min(arr[left], arr[right]))

# Time Complexity: O(log n)
# Binary Search halves the search space in every iteration.

# Space Complexity: O(1)
# Only a few extra variables (left, right, mid, diff1, diff2) are used.

