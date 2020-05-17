# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack =[]
        slow = head
        fast = head
        
        if slow:
            stack.append(slow.val)
            
        else:
            return True
        
        while fast and fast.next:
            slow = slow.next
            
            stack.append(slow.val)
            
            fast = fast.next.next
            
        if fast == None:
            stack.pop()
            
        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
        return True
            
            
            
        
