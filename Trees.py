class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value


# Binary Search Tree (BST) faster searching (O(log n)) for sorted data.
class bst:
    def __init__(self,value):
        self.root = Node(value)
    
    def insert(self,value):
        def _insert(current,value):
            if value < current.value:
                if current.left:
                    _insert(current.left,value)
                else:
                    current.left = Node(value)
            else:
                 if current.right:
                    _insert(current.right,value)
                 else:
                    current.right = Node(value)

            _insert(self.root,value)

    def inorder(node):
        if Node:
            inorder(Node.left)
            print(Node.value, end=" ")
            inorder(Node.right)

bst = bst(10)
bst.insert(5)
bst.insert(15)
bst.insert(8)

# Trie (Prefix Tree)
# A tree used to store strings where each node represents a character.
# Efficient for prefix-based searching, autocomplete, spell-checking.
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end = True

