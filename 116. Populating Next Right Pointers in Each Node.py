"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = collections.deque([root])
        sublist =collections.deque()
        
        while q:
            lenq = len(q)
            for i in range(lenq):
                node = q.popleft()
                sublist.append(node)
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
            while sublist:
                cur = sublist.popleft()
                cur.next = sublist[0] if sublist else None
        return root
