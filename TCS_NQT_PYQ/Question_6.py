## Kth Best-Selling Product Using Min Heap ##

# Problem Statement:

# Amazon is preparing for its annual shopping festival and wants to identify its top-performing products.
# Given the sales count of different products, find the Kth best-selling product.
# The Kth best-selling product is the product whose sales rank is exactly K when all products are sorted in descending order of sales.
# To optimize memory and performance for large datasets, the solution must use a Min Heap of size K.

# Input Format:
# The first line contains two integers N and K.
# The second line contains N integers representing the sales count of each product.

# Output Format:
# Print the Kth best-selling product's sales count.

# Constraints:
# 1≤K≤N≤10^5
# Sales count is a positive integer.

# Example
# Input
# 6 3
# 50 20 70 40 90 60
# Output
# 60
# Explanation
# Sorted in descending order:
# 90 70 60 50 40 20
# The 3rd best-selling product has 60 sales.

import heapq

# Input the number of products and the value of K
n, k = map(int, input().split())

# Input the sales count of all products
arr = list(map(int, input().split()))

# Create a Min Heap using the first K elements
heap = arr[:k]
heapq.heapify(heap)

# Process the remaining elements
for i in range(k, n):

    # If the current element is larger than the
    # smallest element in the heap
    if arr[i] > heap[0]:

        # Remove the smallest element
        heapq.heappop(heap)

        # Insert the current element
        heapq.heappush(heap, arr[i])

# The root of the Min Heap is the Kth largest element
print(heap[0])

# Approach: Min Heap (Priority Queue)

# Time Complexity: O(N log K)
# Each insertion/removal from the heap takes O(log K).

# Space Complexity: O(K)
# The heap stores only K elements.