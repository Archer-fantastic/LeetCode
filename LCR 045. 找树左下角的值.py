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

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        l = [(root, 1)]
        ans = []
        while len(l) != 0:
            node, idx = l.pop(0)
            ans.append((node.val, idx))
            if node.left is not None and node.left.val is not None:
                l.append((node .left, idx + 1))
            if node.right is not None and node.right.val is not None:
                l.append((node.right, idx + 1))
        # print(ans)
        res = [[] for _ in range(ans[-1][-1])]
        for node, idx in ans:
            res[idx - 1].append(node)
        print(res)
        return res[-1][0]
tree1 = bulid_tree([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])
tree2 = bulid_tree([1,2,3,4,5,6,7,8,9,10,11,12,13])
tree3 = bulid_tree([2,1,3])
tree4 = bulid_tree([1,2,3,4,None,5,6,None,None,None,None,7])
s = Solution()
print(s.findBottomLeftValue(tree1))
print(s.findBottomLeftValue(tree2))
print(s.findBottomLeftValue(tree3))
print(s.findBottomLeftValue(tree4))
