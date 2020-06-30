# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        """
        stack = []
        
        if not root:
            return
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if stack:
                node.right = stack[-1]
            node.left = None
            
        
