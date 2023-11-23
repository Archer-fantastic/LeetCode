# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = [(root,1)]
        ans = []
        while len(l) != 0:
            node,idx = l.pop(0)
            if node is not None:
                ans.append((node.val,idx))
                if node.left is not None and node.left.val is not None:
                    l.append((node.left,idx+1))
                if node.right is not None and node.right.val is not None:
                    l.append((node.right,idx+1))
        # print(idx+1)

        res = [[] for _ in range(idx)]

        for node,idx1 in ans:
            res[idx1-1].append(node)

        return res