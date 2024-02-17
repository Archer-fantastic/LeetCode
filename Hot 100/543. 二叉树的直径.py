from typing import Optional, List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def bulid_tree(l):
    l.insert(0,None)
    return init_tree(l,1)
def init_tree(l,idx):
    # l = [null,1,2,3,4,5,null,6,7,null,null,null,null,8]
    if idx >= len(l):
        return None
    if l[idx] is None:
        return None
    tree = TreeNode(l[idx])
    if idx * 2 >= len(l):
        tree.left = None
    if idx * 2 + 1 >= len(l):
        tree.right = None
    tree.left = init_tree(l,2*idx)
    tree.right = init_tree(l,2*idx+1)
    return tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
    def __init__(self):
        self.max_depth = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def inOrder(root):
            if not root:
                return
            self.max_depth = max(self.max_depth,self.maxDepth(root.left) + self.maxDepth(root.right))
            inOrder(root.left)
            inOrder(root.right)
        inOrder(root)
        return self.max_depth
