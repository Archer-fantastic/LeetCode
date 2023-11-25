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
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        te = [0] * 10  # directly use a list to record the element the appearance nums

        def dfs(node):
            te[node.val] += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if not node.left and not node.right:
                if check(te):
                    self.ans += 1
            te[node.val] -= 1

        def check(t):
            n = len(t)
            cnt = 0
            for i in range(n):
                if t[i] % 2:
                    cnt += 1
                    if cnt > 1:
                        break
            return True if cnt <= 1 else False

        dfs(root)
        return self.ans


s = Solution()
print(s.pseudoPalindromicPaths(bulid_tree([2,3,1,3,1,None,1])))