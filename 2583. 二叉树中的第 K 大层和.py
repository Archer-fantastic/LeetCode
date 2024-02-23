# Definition for a binary tree node.
import heapq
from typing import Optional, List


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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def findKthLargest(nums: List[int], k: int) -> int:
            # 先将前k个元素入堆
            heap = [nums[i] for i in range(0, k)]
            heapq.heapify(heap)
            for i in range(k, len(nums)):
                if nums[i] > heap[0]:
                    heapq.heappop(heap)  # 弹出堆顶元素
                    heapq.heappush(heap, nums[i])  # nums[i] 入堆
            return heap[0]
        l = [(root, 1)]
        ans = []
        while len(l) != 0:
            node, idx = l.pop(0)
            ans.append((node.val, idx))
            if node.left is not None and node.left.val is not None:
                l.append((node.left, idx + 1))
            if node.right is not None and node.right.val is not None:
                l.append((node.right, idx + 1))
        # print(ans)
        res = [0 for _ in range(ans[-1][-1])]
        for node, idx in ans:
            res[idx - 1] += node
        print(res)
        if len(res) < k:
            return -1
        return findKthLargest(res,k)


# tree = bulid_tree([3, 9, 20, None, None, 15, 7])
s = Solution()
# tree1 = bulid_tree([1,2,3,4,5,6,7,8,9])
# tree2 = bulid_tree([1,2,2,3,3,None,None,4,4])
# tree3 = bulid_tree([1,2,2,3,None,None,3,4,None,None,4])

tree1 = bulid_tree([6,7,8,2,7,1,3,9,None,1,4,None,None,None,5])
tree2 = bulid_tree([1,2,3,4,5,6,7,8,9,10,11,12,13])
tree3 = bulid_tree([5,8,9,2,1,3,7,4,6])
tree4 = bulid_tree([1,2,None,3])
tree5 = bulid_tree([5,8,9,2,1,3,7])
# print(s.kthLargestLevelSum(tree3, k = 2))
# print(s.kthLargestLevelSum(tree4, k = 1))
print(s.kthLargestLevelSum(tree5, k = 4))
