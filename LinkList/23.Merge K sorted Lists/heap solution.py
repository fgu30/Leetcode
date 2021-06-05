# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# priority Q
# O (k*m*log(k))

import heapq as hq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        for node in lists:
            while node != None:
                hq.heappush(heap,node.val)
                node = node.next
        dum = cur = ListNode()
        n = len(heap)
        while(n > 0):
            cur.next = ListNode(hq.heappop(heap))
            cur = cur.next
            n -= 1
        return dum.next