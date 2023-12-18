from typing import Optional


# Definition for a binary tree node.
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
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l = [(root,1)]
        ans = []
        while len(l) != 0:
            node,idx = l.pop(0)
            ans.append((node,idx))
            if node.left is not None and node.left.val is not None:
                l.append((node.left,idx+1))
            if node.right is not None and node.right.val is not None:
                l.append((node.right,idx+1))

        # print(ans)
        res = [[] for _ in range(ans[-1][-1])]
        for node,idx in ans:
            res[idx-1].append(node)
        for idx in range(1,len(res),2):
            tmp = [t.val for t in res[idx][::-1]]
            for i,t in enumerate(tmp):
                res[idx][i].val = t
        return root

tree = bulid_tree([2,3,5,8,13,21,34])
s = Solution()
print(s.reverseOddLevels(tree))