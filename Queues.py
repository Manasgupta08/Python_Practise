# A queue is a linear data structure that follows the FIFO principle: First In, First Out.
# Basic Operations
# Operation	Description
# enqueue()	Add element to the rear (end) of queue
# dequeue()	Remove element from the front of queue
# peek()	Get front element without removing it
# isEmpty()	Check if queue is empty

# Queue Implementation in Python (using List)
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# now using a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __init__(self, value):
        self.front = None
        self.rear = None
    def enqueue(self,value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front == None:
            return 'queue empty'
        else:
            self.front = self.front.next

# PART 2: Queue Variants
# 1. Deque (Double-Ended Queue)
# A deque allows insertions and deletions from both ends.
# Python provides collections.deque which is faster than list for queue operations.
# 1. Deque (Double-Ended Queue)
# A deque allows insertions and deletions from both ends.
# Python provides collections.deque which is faster than list for queue operations.
from collections import deque

dq = deque()

dq.append(10)         # Add to rear
dq.appendleft(20)     # Add to front
dq.pop()              # Remove from rear
dq.popleft()          # Remove from front


# Monotonic Queue (for Sliding Window Maximum)
# Maintains elements in monotonic increasing or decreasing order.
from collections import deque

def sliding_window_max(nums, k):
    q = deque()
    result = []

    for i in range(len(nums)):
        # Remove out of window elements
        if q and q[0] <= i - k:
            q.popleft()

        # Maintain decreasing order
        while q and nums[i] > nums[q[-1]]:
            q.pop()

        q.append(i)

        if i >= k - 1:
            result.append(nums[q[0]])

    return result

