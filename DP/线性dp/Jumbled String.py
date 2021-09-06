class Solution:
    def TotalWays(self, str):
    mod = 1000000007
    # Code here
    str2 = 'GEEKS'
    n = len(str2)
    m = len(str)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(m+1):
        dp[n][i] = 1
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if str2[i] == str[j]:
                dp[i][j] = (dp[i][j+1] % mod + dp[i+1][j+1] % mod) % mod
            else:
                dp[i][j] = dp[i][j+1]
    return dp[0][0]