### inoder and preoder的list里的数字 是unique的
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def solve(preleft,preright,inleft,inright):
            ##base case
            if(preleft > preright or inleft > inright):
                return None
            root = TreeNode(preorder[preleft])
            mid = inorder.index(preorder[preleft])
            root.left = solve(preleft+1,mid - inleft + preleft,inleft,mid -1)
            root.right = solve(mid - inleft+ preleft+1,preright,mid+1,inright)
            return root
        return solve(0,len(preorder)-1,0,len(inorder)-1)   