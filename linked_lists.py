# A Linked List is a linear data structure where each element (called a node) contains:
# A pointer/reference to the next node in the sequence.
# Unlike arrays, linked lists don’t use contiguous memory, making insertion and deletion more efficient in certain cases.
# Types of Linked Lists
# Singly Linked List	Each node points to the next node only.
# Doubly Linked List	Each node points to both next and previous nodes.
# Circular Linked List	Last node connects back to the head. Can be singly or doubly circular.

# singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        return
        curr = self.head
        while curr != None:
            curr = curr.next 
        curr.next = new_node

# Doubly Linked List
# Each node has:
# data
# prev (points to previous node)
# next (points to next node)
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return 
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current



# reversal of an linked list\
def reversal_ll(self):
    prev_node = None
    curr_node = self.head

    while curr_node != None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
    self.head = prev_node

# Cycle Detection (Floyd’s Tortoise & Hare)
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# merge two sorted linked list
def merge_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 or l2  # Append the rest
    return dummy.next



y