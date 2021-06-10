# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None):
            return head
        f = head.next
        s = head #mid 
        while(f != None and f.next != None):
            f = f.next.next
            s = s.next
        mid = s.next
        s.next = None #cut into 2 linkedlist
        left = self.sortList(head)
        right = self.sortList(mid)
        #merge
        h = res = ListNode(0)
        while left and right:
            if left.val < right.val: h.next, left = left, left.next
            else: h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next 
    # def merge(self,node1,node2):
    #     if node1 == None:
    #         return node2
    #     if node2 == None:
    #         return node1
    #     if node1.val < node2.val:
    #         node1.next = self.merge(node1.next,node2)
    #         return node1
    #     if node1.val >= node2.val:
    #         node2.next = self.merge(node2.next,node1)
    #         return node2 
        
        