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
    def recur(self,L, R):
        if not L and not R: return True
        if not L or not R or L.val != R.val: return False
        return self.recur(L.left, R.right) and self.recur(L.right, R.left)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return not root or self.recur(root.left, root.right)



s = Solution()
tree1 = bulid_tree([1,2,2,None,3,None,3])
tree2 = bulid_tree([1,2,2,2,None,2])
print(s.isSymmetric(root = tree1 ))
print(s.isSymmetric(root = tree2 ))