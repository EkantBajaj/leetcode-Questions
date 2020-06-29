# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.res = None
        def inorder(root):
            if not root or self.res:
                return
            inorder(root.left)
            if root.val > p.val and not self.res:
                self.res=root
            inorder(root.right)
            
        inorder(root)
        return self.res
        
    
            
        
