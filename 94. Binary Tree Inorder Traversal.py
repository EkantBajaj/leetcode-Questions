# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        result=[]
        st = []

        current = root
        while True:
            if current :
                st.append(current)
                current = current.left
            elif st:
                current = st.pop()
                result.append(current.val)
                current = current.right
            else:
                break
                
        return result
        
