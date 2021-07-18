class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        stk1 = [root]
        stk2 = []
        ans = []
        
        while stk1:
            node = stk1.pop()
            stk2.append(node)
            if node.left:
                stk1.append(node.left)             
            if node.right:
                stk1.append(node.right)        
        while stk2:
            ans.append(stk2.pop().val)
        return ans