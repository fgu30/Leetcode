
## recursion
class Solution:
    def mergeTwoLists(self, node1: ListNode, node2: ListNode) -> ListNode:
        if node1 == None:
            return node2
        if node2 == None:
            return node1
        if node1.val < node2.val:
            node1.next = self.mergeTwoLists(node1.next,node2)
            return node1
        if node1.val >= node2.val:
            node2.next = self.mergeTwoLists(node2.next,node1)
            return node2