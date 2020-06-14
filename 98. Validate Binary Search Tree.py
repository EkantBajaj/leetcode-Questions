# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            output.append(root.val)
            inOrder(root.right)
        inOrder(root)
        
        for i in range(1,len(output)):
            if output[i-1]>=output[i]:
                return False
        return True
