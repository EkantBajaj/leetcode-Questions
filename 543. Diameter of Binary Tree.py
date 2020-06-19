# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.maxi = -float('inf')
        
        def dfs(root):
            if root == None:
                return 0
            left = dfs(root.left)
            right= dfs(root.right)
            
            self.maxi = max(self.maxi,left+right)
            
            return max(left,right)+1
        
        dfs(root)
        return max(self.maxi,0)
