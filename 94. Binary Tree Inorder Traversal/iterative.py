class Solution:
       
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stk = []
        while stk or root:
            while root:
                stk.append(root)
                root = root.left
            root = stk.pop()
            ans.append(root.val)
            root = root.right
        return ans