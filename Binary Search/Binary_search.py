# find the element using Binary Search:-
# array = [1,2, 3, 4, 5,6 9, 10, 20, 21, 22] , target = 20

arr = [1, 2, 3, 4, 5, 6, 9, 10, 20, 21, 22]
target = 20
left = 0 # Pointing to the first index of the array.
right = len(arr) - 1 # Pointing to the last index of the array.
while left <= right:
    mid = left + (right -left) // 2 # We are calculating the mid index by taking the avergage of left and right index.
    if arr[mid] == target:
        print("Element found at index: ", mid) # 
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# Time complexity in this case is O(n log n) because we are dividing the array into half in each iteration.
# Space complexity in this case is O(1) because we are not using any extra space.