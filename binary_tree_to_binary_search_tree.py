


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def inorder(root,arr):
    if root is None:
        return
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)

def binary_to_bst(root, arr):
    if root is None:
        return
    binary_to_bst(root.left, arr)
    root.data = arr.pop(0)
    binary_to_bst(root.right, arr)
    


    
root = Node(4)
root.left = Node(2)
root.right = Node(1)
root.left.left = Node(5)
root.left.right  = Node(7)
root.right.left = Node(12)
arr = [] #deque([])#arr.popleft()
inorder(root,arr)
print arr
arr.sort()
print arr
binary_to_bst(root, arr)
b= []
inorder(root, b)
print b
