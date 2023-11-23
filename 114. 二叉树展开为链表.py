# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        node_list = []
        def FrontOrder(root):
            if root is None:
                return
            node_list.append(root)
            print(root.val,end=" ")
            FrontOrder(root.left)
            FrontOrder(root.right)
        FrontOrder(root)
        tmp = root
        for node in node_list[1:]:
            tmp.right = node
            tmp.left = None
            tmp = node
        return root