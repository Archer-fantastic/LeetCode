import collections
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"[{self.val},{self.left},{self.right}]"


def bulid_tree(l):
    l.insert(0, None)
    return init_tree(l, 1)


def init_tree(l, idx):
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
    tree.left = init_tree(l, 2 * idx)
    tree.right = init_tree(l, 2 * idx + 1)
    return tree


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        def dfs(root, low, high):
            if not root:
                return
            dfs(root.left, low, high)
            if low <= root.val <= high: self.sum += root.val
            dfs(root.right, low, high)
        dfs(root,low,high)
        return self.sum
    def rangeSumBST2(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST2(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST2(root.left, low, high)
        return root.val + self.rangeSumBST2(root.left, low, high) + self.rangeSumBST2(root.right, low, high)
    def rangeSumBST3(self, root: TreeNode, low: int, high: int) -> int:
        total = 0
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                continue
            if node.val > high:
                q.append(node.left)
            elif node.val < low:
                q.append(node.right)
            else:
                total += node.val
                q.append(node.left)
                q.append(node.right)

        return total
s = Solution()
print(s.rangeSumBST2(bulid_tree([10,5,15,3,7,None,18]),7,15))
print(s.rangeSumBST2(bulid_tree([10,5,15,3,7,13,18,1,None,6]),6,10))
