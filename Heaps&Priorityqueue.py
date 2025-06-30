# Heap
# A heap is a specialized binary tree (often implemented as an array) that satisfies the heap property:
# In a Min Heap, the parent is less than or equal to its children.
# In a Max Heap, the parent is greater than or equal to its children.

#  Priority Queue
# A priority queue is an abstract data type where each element is associated with a priority, and elements with higher priority are served before elements with lower priority.
# Heaps are the underlying data structure used to implement efficient priority queues.

# Common Heap-Based Problems

import heapq
heap = []
def func1(nums,k):
    for num in nums:
        heapq.heappush(heap,num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap

nums = [5, 1, 9, 3, 7, 6]
k = 3
print(func1(nums,2))

# Median in a Data Stream
# Problem: Continuously calculate the median of numbers from a data stream.
class stream_median:
    def __init__(self):
        self.left = []
        self.right = []
    def add_num(self,num):
        heapq.heappush(self.left,-nums)        
        heapq.heappush(self.right,-heapq.heappop(self.left))

        if len(self.right) > (self.left):
            heapq.heappush(self.left,-heapq.heappop(self.right))

    def get_median(self):
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2.0        
