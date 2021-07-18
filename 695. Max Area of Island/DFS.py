class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        def dfs(i,j):
            if grid[i][j] == 0:
                return 0
            if i < 0 or j < 0 or i >= m or j >= n:
                return 0
            #only valid left
            grid[i][j] = 0
            return 1 + dfs(i+1,j) + dfs(i-1,j)\
                    + dfs(i,j-1) + dfs(i,j+1)
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:     
                    tmp = dfs(i,j)
                    ans = max(ans,tmp)

        return ans

if __name__ == '__main__':
    arr = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    testcase = Solution()
    print(testcase.maxAreaOfIsland(arr))
    
    