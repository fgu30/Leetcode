# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseL(head,tail):
            prev = None
            p = head
            while prev != tail:
                nxt = p.next
                p.next = prev
                prev,p = p,nxt
            
            return tail,head
        
        dum = ListNode(-1)
        dum.next = head
        pre = dum
        
        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if tail == None:
                    return dum.next
            nxt = tail.next
            head,tail = reverseL(head,tail)
            pre.next = head
            tail.next = nxt
            pre = tail
            head = nxt
        return dum.next
                
                
        