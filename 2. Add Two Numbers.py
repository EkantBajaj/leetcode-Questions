class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        newl3 = ListNode()
        c = 0
        l3 = newl3
        while l1 and l2:
            sum = l1.val+l2.val+c
            c = sum//10
            val=sum%10
            l3.next = ListNode(val)
            l1 = l1.next
            l2 = l2.next
            l3=l3.next
            
        while l1:
            l3.next = ListNode((l1.val+c)%10)
            c = (l1.val+c)//10
            l1 = l1.next
            l3 = l3.next
        while l2:
            l3.next = ListNode((l2.val+c)%10)
            c = (l2.val+c)//10 
            print(l2.val,l2.next)
            l2 = l2.next
            l3 = l3.next
        
        if c :
            l3.next = ListNode(c)
        return newl3.next
