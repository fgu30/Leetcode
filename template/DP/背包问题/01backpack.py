## 朴素版本
n,m = map(int,input().split())
# n 物品
# m 是体积
p = [0]*(n+1)
for _ in range(1,n+1):
    l1,l2 =  map(int,input().split())
    p[_] = (l1,l2)
    
dp = [[0]*(m+1) for _ in range(n+1)]
def solve():
    for i in range(1,n+1):
        v,w = p[i]
        for j in range(1,m+1):
            if v <= j:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-v] + w)
            else:
                dp[i][j] = dp[i-1][j]
solve()
print(dp[n][m])


# 优化版本

n,m = map(int,input().split())
# n 物品
# m 是体积
f = [0]*(m+1)
def solve():
    for i in range(1,n+1):
        v,w = map(int,input().split())
        for j in range(m,v-1,-1):
            f[j] = max(f[j],f[j-v] + w)
            

solve()
print(f[m])