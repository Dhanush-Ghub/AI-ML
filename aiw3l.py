class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def isSymmetricTree(root):
    if not root:
        return True
    
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.value == right.value and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    return isMirror(root.left, root.right)

def buildTreeFromInput(values, index):
    if index >= len(values) or values[index] == -1:
        return None
    root = TreeNode(values[index])
    root.left = buildTreeFromInput(values, 2 * index + 1)
    root.right = buildTreeFromInput(values, 2 * index + 2)
    return root

input_str = input("Enter binary tree values (-1 for null nodes): ")
values = list(map(int, input_str.split()))
root = buildTreeFromInput(values, 0)

if isSymmetricTree(root):
    print("Symmetric")
else:
    print("Not symmetric")
