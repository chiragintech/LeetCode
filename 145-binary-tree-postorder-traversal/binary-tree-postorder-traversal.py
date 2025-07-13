# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        l = []
        l += self.postorderTraversal(root.left)
        l += self.postorderTraversal(root.right)
        l += [root.val]
        return l