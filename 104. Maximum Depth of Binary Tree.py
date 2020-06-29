# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def helper(root):
            if root.left == root.right and root.right ==None:
                return 0
            
            left = helper(root.left) if root.left else 0
            right = helper(root.right)if root.right else 0
            
            return max(left,right)+1
        return helper(root)+1
        
