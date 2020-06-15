# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        direction = -1
        q = queue.Queue()
        res = []
        if not root:
            return root
        q.put(root)
        while not q.empty():
            direction = -direction
            a = []
            size = q.qsize()
            
            while size:
                cur = q.get()
                if direction == 1:
                    a.append(cur.val)
                else:
                    a.insert(0,cur.val)
                if cur.left:
                    q.put(cur.left)
                if cur.right:
                    q.put(cur.right)
                size -=1
            if a:
                res.append(a)
        return res
