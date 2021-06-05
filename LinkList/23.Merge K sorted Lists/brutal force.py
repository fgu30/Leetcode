# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# O(k*k*n) trash


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dum = cur =  ListNode()
        n = len(lists)
        
        while(True):
            min_value = float('inf')
            p = -1
            none_p = -1
            for i in range(len(lists)):
                if lists[i] == None:
                    none_p = i
                else:
                    if lists[i].val <= min_value:
                        min_value = lists[i].val
                        p = i


            if min_value == float('inf'):
                break;
            cur.next = ListNode(min_value)
            cur = cur.next
            lists[p] = lists[p].next
            if none_p != -1:
                lists.pop(none_p)
        return dum.next