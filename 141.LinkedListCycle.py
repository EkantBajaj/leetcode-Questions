# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head and head.next:
            slow = head
            fast = head.next.next
        else:
            return False
        while slow and fast and fast.next:
            if slow == fast:
                return True
            slow =slow.next
            fast = fast.next.next
        return False
