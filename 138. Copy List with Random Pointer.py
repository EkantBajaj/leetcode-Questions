"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        node_map = {}
        
        current = head
        newHead = Node(current.val)
        node_map[current]=newHead
        newcurrent = newHead
        while current:
            if current in node_map:
                newcurrent = node_map[current]
            else:
                newcurrent = Node(current.val)
                node_map[current]=newcurrent
            if current.next and current.next in node_map:
                newcurrent.next = node_map[current.next]
            elif current.next:
                newcurrent.next = Node(current.next.val)
                node_map[current.next]= newcurrent.next
            if current.random and current.random in node_map:
                newcurrent.random = node_map[current.random]
            elif current.random:
        
                newcurrent.random = Node(current.random.val)
                node_map[current.random]= newcurrent.random
            current = current.next
            
        return newHead
            
        
