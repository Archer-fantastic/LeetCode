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

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        nodes = {}
        fa = {}
        if root:
            fa[root.val] = -1
        global _len
        _len = 0
        def get_nodes(root):
            if root:
                global _len
                nodes[root.val] = []
                _len += 1
                if root.left:
                    nodes[root.val].append(root.left.val)
                    fa[root.left.val] = root.val
                if root.right:
                    nodes[root.val].append(root.right.val)
                    fa[root.right.val] = root.val
                get_nodes(root.left)
                get_nodes(root.right)
        get_nodes(root)
        for node in nodes:
            if fa[node] != -1:
                nodes[node].append(fa[node])
        print(nodes)
        print(_len)
        infect = []
        stk = [start]
        res = 0
        while len(stk) > 0:
            node = stk.pop()
            infect.append(node)
            for t in nodes[node]:
                if t not in infect:
                    stk.append(t)


tree1 = bulid_tree([1,5,3,None,4,10,6,None,None,9,2])

s = Solution()
print(s.amountOfTime(tree1,3))