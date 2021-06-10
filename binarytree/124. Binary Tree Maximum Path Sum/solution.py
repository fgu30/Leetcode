class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        maxValue = float('-inf')
        def dfs(root):
            nonlocal maxValue
            if root is None:
                return 0
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            tmp = root.val + left + right
            maxValue = max(maxValue,tmp)
            return root.val + max(left,right)
        dfs(root)
        return maxValue