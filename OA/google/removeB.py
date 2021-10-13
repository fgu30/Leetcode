def solve(s):
    n = len(s)
    dp = [0]*(n)
    if n == 1:
        return 1 if s[0] == 'b' else 0
    for i in range(1,n):
        if s[i] == 'a':
            dp[i] = dp[i-1]
        else:
            dp[i] = min(dp[i-1] + 2,i+1)

    f = [0]*n
    for i in range(n-2,-1,-1):
        if s[i] == 'a':
            f[i] = f[i+1]
        else:
            f[i] = min(f[i+1] + 2,n-i)
    res = float('inf')
    for i in range(n):
        res = min(res,dp[i] + f[i])
        
    return res
            
print(solve('abbaaba'))            
        