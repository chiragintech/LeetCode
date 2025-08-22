# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def find(node):
            if not node:
                return 0
            left = find(node.left)
            right = find(node.right)
            return 1 + max(left, right)
        def check(node):
            if not node:
                return True
            left = find(node.left)
            right = find(node.right)
            if abs(left-right) > 1:
                return False
            return check(node.left) and check(node.right)
        if not root:
            return True
        return check(root)
        
