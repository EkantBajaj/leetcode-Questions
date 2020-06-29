# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder and postorder:
            ind = inorder.index(postorder.pop())
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(inorder[:ind],postorder[:ind])
            root.right = self.buildTree(inorder[ind+1:],postorder[ind:])
            return root