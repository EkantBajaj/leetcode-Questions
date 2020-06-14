# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        def merge(head1,head2):
            newHead = ListNode()
            current = newHead
            
            while head1 and head2:
                if head1.val < head2.val:
                    current.next = head1
                    head1= head1.next
                else:
                    current.next=head2
                    head2 = head2.next
                current = current.next
                
            if head1:
                current.next = head1
            if head2:
                current.next = head2
                
            return newHead.next
        
        merged_list = lists.pop()
        
        while lists:
            list = lists.pop()
            merged_list = merge(list,merged_list)
        
        return merged_list
        
        
