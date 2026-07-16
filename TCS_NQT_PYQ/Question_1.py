# Problem Statement:
# There are two items A and B with their respective prices.
# Write a program to determine which item is more expensive.

# Conditions:
# If either price is less than 0, print "Invalid input".
# If both prices are equal, print "Prices equal".
# Otherwise, print the higher price followed by "is more expensive".

# Example 1
# Input
# 10 15
# Output
# 15 is more expensive

# Example 2
# Input
# 10 10
# Output
# Prices equal

A, B = map(int,input().split())

if A < 0 or B < 0:
    print("Invalid Input")
elif A == B:
    print("Prices equal")
elif A > B :
    print(A,"is more expensive")
else:
    print(B,"is more expensive")
