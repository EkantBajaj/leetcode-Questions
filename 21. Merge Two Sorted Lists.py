# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        def reverseList(head):
            if not head or not head.next:
                return head
            c=head
            p = None
            n = c.next
            while c:
                c.next=p
                p=c
                c=n
                if c:
                    n=c.next
            return p
        new = ListNode(0)
        tail = new
        new.next = head
        start = head
        
        
        while True:
            end = start
            for i in range(k-1):
                if not end:
                    break
                end =end.next
                
            if not end:
                break
            next_start = end.next
            end.next = None
            
            rev = reverseList(start)
            
            tail.next = rev
            tail = start
            start = next_start
        tail.next =next_start
        return new.next
    
        
        
