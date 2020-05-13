# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        curra,currb=headA,headB
        lenA=lenB=0
        while curra:
            lenA +=1
            curra =curra.next
        while currb:
            lenB +=1
            currb =currb.next
        
        diff = abs(lenA-lenB)
        curra,currb=headA,headB
        if lenA>lenB:
            for i in range(diff):
                curra=curra.next
        else:
            for i in range(diff):
                currb= currb.next
                
        while curra and currb:
            if curra == currb:
                return curra
            curra=curra.next
            currb=currb.next
        return None
