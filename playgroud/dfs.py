'''
1 1 0
0 1 1
0 1 0
'''
grid = [[1,1,0],[0,1,1],[0,1,1]]

def solve(grid):
    n,m = len(grid),len(grid[0])
    res = []
    def dfs(i,j,tmp):
        if i < 0 or i >=n or j < 0 or j >= m:
            return
        if grid[i][j] == 0:
            return
        if i == n -1 and j == m -1:
            res.append(tmp[:])
            return 
        tmp.append((i,j))
        for a,b in [(i+1,j),(i,j+1)]:
            dfs(a,b,tmp)
        tmp.pop()
    dfs(0,0,[])
    
    print(res)

solve(grid)
        
