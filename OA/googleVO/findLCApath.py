class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
        
        
def getLCA(root,p,q):
    if not root or root == p or root == q:
        return root
    L = getLCA(root.left,p,q)
    R = getLCA(root.right,p,q)
    if not L:
        return R
    if not R:
        return L
    return root

res = []
def dfs(path,root,node):
    if not root:
        return False
    if root == node:
        res.append(path[:])
        return True
    
    if root.left:
        path.append('left')
        if not dfs(path,root.left,node):
            path.pop()
    if root.right:
        path.append('right')
        if not dfs(path,root.right,node):
            path.pop()



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
    
    p = treeNode5
    q = treeNode7

    lca = getLCA(treeNode1,p,q)
    dfs([],lca,p)
    print(res)