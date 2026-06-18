# find the first occurance of the target in the array:
# array = [1,2,2,2,3, 4, 9, 10] ,target = 2

arr = [1, 2, 2, 2, 3, 4, 9, 10]
target = 2
left = 0 # Pointing to the first index of the array.
right = len(arr) - 1 # Pointing to the last index of the array.
ans = -1 # Initializing a variable to store the index of the first occurance of the target in the array. If the target is not found, it will remain -1.
while left <= right:
    mid = left + (right -left) // 2 # We are calculating the mid index by taking the avergage of left and right index.
    if arr[mid] == target:
        ans = mid # If the target is found, we store the index in the ans variable and continue searching in the left half of the array to find the first occurence of the target.
        right = mid - 1
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

print("First occurence of the target is at index: ", ans)

# Time complexity in this case is O(n log n) because we are dividing the array into half in each iteration.
# Space complexity in this case is O(1) because we are not using any extra space.