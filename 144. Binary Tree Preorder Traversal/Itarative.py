# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stk = []
        while stk or root:
            if root:
                stk.append(root.right)
                ans.append(root.val)
                root = root.left
            else:
                root = stk.pop()
        return ans