# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: 
            return root
        def invert(root):
            if (root.left == root.right)and root.left == None:
                return
            else:
                if root.left:
                    invert(root.left)
                if root.right:
                    invert(root.right)
                root.left,root.right=root.right,root.left
                
        invert(root)
        return root
