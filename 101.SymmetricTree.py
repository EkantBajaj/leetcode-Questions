# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def helper(root1,root2):
            if not root1 and not root2 and root1==None:
                return True
            elif not root1 or not root2:
                return False
            elif root1. val != root2.val:
                return False
            else:
                return (helper(root1.left,root2.right) and helper(root1.right,root2.left))
            
        return helper(root,root)
