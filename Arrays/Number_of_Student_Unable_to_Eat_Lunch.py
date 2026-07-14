# LEETCODE 1700: Number of Students Unable to Eat Lunch

# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. 
# All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) 
# and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). 
# Return the number of students that are unable to eat.

# Example 1:

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.
# Example 2:

# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        count0 = 0
        count1 = 0

        for student in students:
            if student == 0:
                # Count how many students like Circular(0) sandwiches
                count0 += 1
            else:
                # Count how many students like Square(0) sandwiches
                count1 += 1

        # Check every sandwich from top to bottom
        for sandwich in sandwiches:

            #Current sandwich is Circular(0)
            if sandwich == 0:

                # No student likes Circular anymore,
                # so nobody can eat this sandwich.
                # The remaining students will stay hungry.
                if count0 == 0:
                    return count1
                
                # One Circular-loving student eats this sandwich,
                # so one Circular lover becomes less
                count0 -= 1

            # Current sandwich is Square(1)
            else:

                # No student likes Square anymore,
                # so nobody can eat this sandwich.
                if count1 == 0:
                    return count0
                
                # One Square-loving students eats this sandwich,
                # so one Square lover becomes less.
                count1 -= 1

        # Every student got a sandwich
        return 0
    
# Time Complexity: O(n)
# Space Complexity: O(1)