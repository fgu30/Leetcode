# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        p = dummy
        
        while True:
            cnt = k
            stack = []
            tmp = head
            while tmp and cnt:
                stack.append(tmp)
                tmp = tmp.next
                cnt-=1
            if cnt:
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = tmp
            head = tmp
            
        return dummy.next
        
        
        
        