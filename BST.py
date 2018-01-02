class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(root, lo, hi):
    if not root:
        return True
    
    if root.data < lo or root.data > hi:
        return False
    
    return is_bst(root.left, lo, root.data-1) and is_bst(root.right, root.data+1, hi)


def checkBST(root):
    print (is_bst(root.left, 0, root.data-1) and is_bst(root.right, root.data+1, 10000))

