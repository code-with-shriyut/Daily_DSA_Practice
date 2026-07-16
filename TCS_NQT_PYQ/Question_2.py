# Postfix Expression Evaluation

# Problem Statement:
# Create a class that implements a Stack with the following methods:
# push(value: string)
# pop()
# evaluate()

# The stack should be encapsulated, meaning the stack data should be private 
# and can only be accessed through these methods.

# Use this class to evaluate a Postfix Expression.

# It is guaranteed that the input expression is always valid.

# Input Format
# The first line contains an integer N, representing the number of tokens.
# The second line contains N space-separated tokens (numbers and operators).
# Supported Operators
# +
# -
# *
# /
# Output Format

# Print the result of the postfix expression.

# Example 1
# Input
# 5
# 13 5 + 4 -
# Output
# 14
# Explanation
# 13 + 5 = 18

# 18 - 4 = 14

class Stack:

    def __init__(self):
        self.stack = []

    # Push an element into the stack
    def push(self, value):
        self.stack.append(value)

    # Remove and return the top element
    def pop(self):
        return self.stack.pop()

    # Evaluate the postfix expression
    def evaluate(self, tokens):

        for token in tokens:

            # If the token is a number,
            # push it into the stack
            if token not in "+-*/":
                self.push(int(token))

            else:

                # Pop the second operand
                b = self.pop()

                # Pop the first operand
                a = self.pop()

                # Perform the operation
                if token == "+":
                    self.push(a + b)

                elif token == "-":
                    self.push(a - b)

                elif token == "*":
                    self.push(a * b)

                else:
                    self.push(a // b)

        # Final answer is left on the top of the stack
        return self.pop()


# Input
n = int(input())

tokens = input().split()

obj = Stack()

print(obj.evaluate(tokens))