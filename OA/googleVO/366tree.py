class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
        

def solve(root):
    if not root:
        return root
    if not root.left and not root.right:
        res.append(root.val)
        return None
    root.left = solve(root.left)
    root.right = solve(root.right)
    return root
    



if __name__ == '__main__':
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(3)
    treeNode4 = TreeNode(4)
    treeNode5 = TreeNode(5)
    treeNode6 = TreeNode(6)
    treeNode7 = TreeNode(7)
    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode2.left  = treeNode4
    treeNode2.right = treeNode5
    treeNode3.right = treeNode6
    treeNode6.left = treeNode7
    res = []
    solve(treeNode1)
    print(res)


