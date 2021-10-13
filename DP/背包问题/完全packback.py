n,m = map(int,input().split())

    
f = [0]*(m+1)

for i in range(1,n+1):
    v,w = map(int,input().split())
    for j in range(v,m+1):
        f[j] = max(f[j],f[j-v]+w)
            

print(f[m])


----

n,m = map(int,input().split())

    
dp = [[0]*(m+1) for _ in range(n+1)]
def solve():
    for i in range(1,n+1):
        v,w = map(int,input().split())
        for j in range(1,m+1):

            dp[i][j] = dp[i-1][j]
            if v <= j:
                dp[i][j] = max(dp[i][j],dp[i][j-v] + w)
            
                


solve()
print(dp[n][m])