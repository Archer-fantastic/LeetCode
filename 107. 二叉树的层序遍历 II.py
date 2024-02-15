# Definition for a binary tree node.
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

class Solution(object):

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        l = [(root, 1)]
        ans = []
        while len(l) != 0:
            node, idx = l.pop(0)
            if node is not None:
                ans.append((node.val, idx))
                if node.left is not None and node.left.val is not None:
                    l.append((node.left, idx + 1))
                if node.right is not None and node.right.val is not None:
                    l.append((node.right, idx + 1))
        # print("层序遍历结果：", ans)

        res = [[] for _ in range(idx)]

        for node, idx1 in ans:
            res[idx1 - 1].append(node)
        # print("最终分层结果：", res)
        return res[::-1]


tree1 = bulid_tree([3,9,20,None,None,15,7])
tree2 = bulid_tree([1,2,3,4,5,6,7,8,9,10,11])
tree3 = bulid_tree([1])
tree4 = bulid_tree([])

s = Solution()
print(s.levelOrderBottom(tree1))
print(s.levelOrderBottom(tree2))
print(s.levelOrderBottom(tree3))
print(s.levelOrderBottom(tree4))

