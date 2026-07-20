# Time Conversion (12-Hour to 24-Hour Format)

# Problem Statement
# Given a time in 12-hour AM/PM format, convert it to 24-hour (military) format.
# Note
# 12:00:00 AM becomes 00:00:00
# 12:00:00 PM remains 12:00:00
# Function Description
# Complete the timeConversion function.
# The function should return the given time in 24-hour format.
# Function Signature
# def timeConversion(s):

# Input Format:
# A single string s representing the time in 12-hour format.
# Format:
# hh:mm:ssAM
# or
# hh:mm:ssPM

# Output Format:
# Return the equivalent time in 24-hour format.

# Constraints
# All input times are valid.
# Example 1
# Input
# 07:05:45PM
# Output
# 19:05:45
# Example 2
# Input
# 12:01:00AM
# Output
# 00:01:00

# Input the time in 12-hour format
time = input()

# Extract the hour
hour = int(time[:2])

# Extract AM or PM
period = time[-2:]

# Extract minutes and seconds
remaining_time = time[2:-2]

# If the time is AM
if period == "AM":

    # Convert 12 AM to 00
    if hour == 12:
        hour = 0

# If the time is PM
else:

    # Add 12 to all hours except 12 PM
    if hour != 12:
        hour += 12

# Print the converted time
print(f"{hour:02d}{remaining_time}")

# Approach: String Manipulation

# Time Complexity: O(1)
# A fixed number of string operations are performed.

# Space Complexity: O(1)
# Only a few variables are used.