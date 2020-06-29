# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        q = collections.deque([root])
        direction = 1
        sublist =[]
        result =[]
        while q:
            lenq= len(q)
            
            for _ in range(lenq):
                node = q.popleft()
                if direction>0:
                    sublist.append(node.val)
                else:
                    sublist.insert(0,node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if sublist:
                result.append(sublist)
                sublist=[]
                direction = -direction
                    
        return result
        
