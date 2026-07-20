## Determine the Most Expensive Item ##

# Problem Statement:

# There are two items A and B with their respective prices.
# Write a program to determine which item is more expensive.

# Conditions:

# If either price is less than 0, print "Invalid input".
# If both prices are equal, print "Prices equal".
# Otherwise, print the higher price followed by "is more expensive".

# Example 1
# Input:
# 10 15
# Output:
# 15 is more expensive
# Example 2
# Input
# 10 10
# Output
# Prices equal

# Input the prices of both A and B respectively.
A, B = map(int, input().split())

# Check the given conditions:
# 1st Condition: If either price is less than 0, print "Invalid input".
if A < 0 and B < 0:
    print("Invalid input")

# 2nd Condition: If both prices are equal, print "Prices equal".
elif A == B:
    print("Prices equal")

# 3rd Condition: Otherwise, print the higher price followed by "is more expensive".

else:
    print(max(A,B), "is more expensive")