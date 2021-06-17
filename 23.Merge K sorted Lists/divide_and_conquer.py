# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        def mergeTwo(node1,node2):
            if node1 == None:
                return node2
            elif node2 == None:
                return node1
            elif node1.val < node2.val:
                node1.next = mergeTwo(node1.next,node2)
                return node1
            else:
                node2.next = mergeTwo(node1,node2.next)
                return node2
        
        def mergesort(l,r):#return ListNode
            if(l == r):
                return lists[l]
            if(l > r):
                return None
            mid = l + r >>1
            return mergeTwo(mergesort(l,mid),mergesort(mid+1,r))

        return mergesort(0,len(lists) - 1)