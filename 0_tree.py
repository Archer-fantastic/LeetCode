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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = [(root,1)]
        ans = []
        while len(l) != 0:
            node,idx = l.pop(0)
            ans.append((node.val,idx))
            if node.left is not None and node.left.val is not None:
                l.append((node.left,idx+1))
            if node.right is not None and node.right.val is not None:
                l.append((node.right,idx+1))
        # print(ans)
        res = [[] for _ in range(ans[-1][-1])]
        for node,idx in ans:
            res[idx-1].append(node)
        # print(res)
        return res
    def FrontOrder(self, root):
        if root is None:
            return
        self.FrontOrder(root.left)
        if root.val is not None:
            print(root.val,end=' ')
        self.FrontOrder(root.right)
    def __init__(self):
        self.A = []
    def MidOrder(self, root):
        if root is None:
            return
        self.MidOrder(root.left)
        if root.val is not None:
            # print(root.val,end=' ')
            self.A.append(root.val)
        self.MidOrder(root.right)

        print(self.A)
        print(self.A[0],self.A[-1])

    def PostOrder(self, root):
        if root is None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        if root.val is not None:
            print(root.val,end=' ')
    def height(self,root):
        return 0 if root is None else max(self.height(root.left),self.height(root.right)) + 1
    def isBalanced(self, root):
        return True if root is None else abs(self.height(root.left)-self.height(root.right))<2 \
                and self.isBalanced(root.left) and self.isBalanced(root.right)
    def fun(self,root):
        # 找到树最左和最右的数字
        if root is None:
            return
        cur_node1 = root
        cur_node2 = root
        while cur_node1.left is not None:
            cur_node1 = cur_node1.left
        while cur_node2.right is not None:
            cur_node2 = cur_node2.right
        print(cur_node1.val,cur_node2.val)

    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        l = [(root,1)]
        ans = []
        while len(l) != 0:
            node,idx = l.pop(0)
            ans.append((node.val,idx))
            if node.left is not None:
                l.append((node.left,idx+1))
            if node.right is not None:
                l.append((node.right,idx+1))
        # 层序遍历的结果
        print(ans)
        res = [[] for _ in range(ans[-1][-1])]
        for node,idx in ans:
            res[idx-1].append(node)
        print(res)
        return sum(res[-1])





# tree = bulid_tree([3, 9, 20, None, None, 15, 7])
s = Solution()
# tree1 = bulid_tree([1,2,3,4,5,6,7,8,9])
# tree2 = bulid_tree([1,2,2,3,3,None,None,4,4])
# tree3 = bulid_tree([1,2,2,3,None,None,3,4,None,None,4])
# print(s.isBalanced(tree1))
# print(s.isBalanced(tree2))
# print(s.isBalanced(tree3))
# s.FrontOrder(tree)
# print()
# s.MidOrder(tree)
# print()
# s.PostOrder(tree)
# print()
# print(s.levelOrder(tree))
# print()

tree1 = bulid_tree([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])
tree2 = bulid_tree([1,2,3,4,5,6,7,8,9,10,11,12,13])
# s.MidOrder(tree1)
# print(s.A)
# s.fun(tree1)
print(s.deepestLeavesSum(tree1))
print(s.deepestLeavesSum(tree2))
