# A stack is a linear data structure that follows the LIFO principle: Last In, First Out.
# Basic Stack Operations
# Operation	Description
# push()	Add an element to the top of the stack
# pop()	Remove and return the top element
# peek()	View the top element without removing it
# isEmpty()	Check if the stack is empty

# Stack Implementation in Python (using List)
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Monotonic Stack
# A monotonic stack is a stack that maintains its elements in increasing or decreasing order.

# Code: Next Greater Element (NGE)
def next_greater_elements(arr):
    result = [-1] * len(arr)
    stack = []  # Store indices

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)

    return result

# Example
arr = [2, 1, 2, 4, 3]
print(next_greater_elements(arr))  # Output: [4, 2, 4, -1, -1]



