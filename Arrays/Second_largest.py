# Find the second largest number in a list

list = [10, 20, 24, 11, 9]
largest = list[0]
second = list[0]
for i in range(len(list)):
    if list[i] > largest:
        second = largest
        largest = list[i]

print(second)

# Time complexity in this case is O(n) because we are traversing the array once.
# Space complexity in this case is O(1) since we are not using any extra array