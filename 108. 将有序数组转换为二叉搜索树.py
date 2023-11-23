# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return f"[{self.val},{self.left},{self.right}]"

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        left = 0
        right = n - 1
        mid = (left+right+1) // 2
        root = TreeNode(nums[mid])
        if left != mid:
            root.left = self.sortedArrayToBST(nums[:mid])
        if right != mid:
            root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
s = Solution()
print(s.sortedArrayToBST([-10,-3,0,5,9]))