class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        used = [[False]*n for _ in range(m)]

        def dfs(i,j,k):
            if k == len(word):
                return True
            if i < m and i >= 0 and j < n and j >=0 \
                and not used[i][j] and word[k] == board[i][j]:
                    used[i][j] = True
                    if dfs(i-1,j,k+1)\
                    or dfs(i+1,j,k+1)\
                    or dfs(i,j-1,k+1)\
                    or dfs(i,j+1,k+1) == True:
                        return True
                    used[i][j] = False
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False