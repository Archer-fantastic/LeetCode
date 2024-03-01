import modulefinder
from math import inf
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
        # 94 中序遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []

        def dfs(root):
            if not root:
                return []
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)
            return self.arr

        return dfs(root)

    # 104.二叉树的最大深度
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    # 102 二叉树的层序遍历
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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

        res = [[] for _ in range(idx)]

        for node, idx1 in ans:
            res[idx1 - 1].append(node)

        return res
    # 108. 将有序数组转换为二叉搜索树
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        left = 0
        right = n - 1
        mid = (left + right + 1) // 2
        root = TreeNode(nums[mid])
        if left != mid:
            root.left = self.sortedArrayToBST(nums[:mid])
        if right != mid:
            root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    # 543.二叉树的直径
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))
        self.max_depth = 0
        def inOrder(root):
            if not root:
                return
            self.max_depth = max(self.max_depth, maxDepth(root.left) + maxDepth(root.right))
            inOrder(root.left)
            inOrder(root.right)

        inOrder(root)
        return self.max_depth

    # 226. 翻转二叉树
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        # 98.验证二叉搜索树
    def isValidBST(self, root: Optional[TreeNode], left=-inf, right=inf) -> bool:
        if not root:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left,left,x) and self.isValidBST(root.right,x,right)
    #230. 二叉搜索树中第K小的元素
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.arr = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.arr[k-1]
#     199. 二叉树的右视图
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
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
        print(res)
        return [num[-1] for num in res]
#    114. 二叉树展开为链表
    def flatten(self, root: Optional[TreeNode]) -> None:
        head = TreeNode()
        p = head
        self.A = []
        def dfs(root):
            if not root: return
            self.A.append(root)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        for a in self.A:
            a.left = None
            a.right = None
            p.right = a
            p = p.right
        return head.right
    # 105.从前序与中序遍历序列构造二叉树
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        node = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        node.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return node
    # 236. 二叉树的最近公共祖先
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

# 144. 二叉树的前中后序遍历

    def preorderTraversal(self, root):
        ans = []
        if not root : return
        s = [root]
        while len(s) != 0:
            node = s[-1]
            if node.left:
                s.append(node.left)

            ans.append(node)
            if node.right:
                s.append(node.right)
        return ans

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans, stk = [], []
        while root or stk:
            if root:
                stk.append(root)
                root = root.left
            else:
                root = stk.pop()
                ans.append(root.val)
                root = root.right
        return ans


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if root is None:
            return ans
        stk = [root]
        while stk:
            node = stk.pop()
            ans.append(node.val)
            if node.left:
                stk.append(node.left)
            if node.right:
                stk.append(node.right)
        return ans[::-1]
    # 236. 二叉树的最近公共祖先
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is p or root is q or p is q: return p
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root
        if left: return left
        if right: return right
        return root

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val: p,q = q,p
        if p.val<=root.val<=q.val: return root
        if root.val<p.val<q.val: return self.lowestCommonAncestor(root.right,p,q)
        if p.val<q.val<root.val: return self.lowestCommonAncestor(root.left,p,q)

s = Solution()
# print(s.inorderTraversal(bulid_tree([1,None,2,3])))
# print(s.kthSmallest(bulid_tree([5,3,6,2,4,None,None,1]),3))
print(s.lowestCommonAncestor(bulid_tree([3,5,1,6,2,0,8,None,None,7,4])))