# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"[{self.val},{self.left},{self.right}]"
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
    # tree.left = TreeNode(l[idx*2])
    # tree.right = TreeNode(l[idx*2+1])
    tree.left = init_tree(l,2*idx)
    tree.right = init_tree(l,2*idx+1)
    return tree

class Solution(object):
    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        # left = self.get_len(root.left)
        right = self.get_len(root.right)
        if k == right == 1:
            return root.right.val
        if root and right + 1 == k:
            return root.val
        if right >= k:
            return self.kthSmallest(root.right,k)
        else:
            return self.kthSmallest(root.left,k-right-1)

    def get_len(self,root):
        if not root:
            return 0
        return self.get_len(root.left) + self.get_len(root.right) + 1
    def kthSmallest3(self, root: Optional[TreeNode], k: int) -> int:
        left = self.get_len(root.left)
        if root and left + 1 == k:
            return root.val
        if left >= k:
            return self.kthSmallest(root.left,k)
        else:
            return self.kthSmallest(root.right,k-left-1)
    def __init__(self):
        self.A = []
    def MidOrder(self, root):
        if root is None:
            return
        self.MidOrder(root.left)
        if root.val is not None:
            self.A.append(root.val)
        self.MidOrder(root.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.MidOrder(root)
        return self.A[k-1]

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def fun(root,p,q):
            if p.val <= root.val <= q.val:
                return root
            if p.val <= q.val <= root.val:
                return self.lowestCommonAncestor(root.left,p,q)
            return self.lowestCommonAncestor(root.right,p,q)
        if p.val > q.val:
            p,q = q,p
        return fun(root,p,q)
s = Solution()
# print(s.kthSmallest2(bulid_tree([5,3,6,2,4,None,None,1]),3))
# print(s.kthSmallest(bulid_tree([5,3,6,2,4,None,None,1]),3))
# print(s.kthSmallest(bulid_tree([3,1,4,None,2]),1))
#
# print(s.kthSmallest(bulid_tree([i for i in range(1,16)]),15))

print(s.lowestCommonAncestor(bulid_tree([6,2,8,0,4,7,9,None,None,3,5]),TreeNode(2), TreeNode(4)))
print(s.lowestCommonAncestor(bulid_tree([2,1]),TreeNode(2), TreeNode(1)))