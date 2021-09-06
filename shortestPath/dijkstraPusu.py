https://www.acwing.com/activity/content/problem/content/918/1/

n,m = map(int,input().split())

graph = [[float("inf") for i in range(n+1)] for j in range(n+1)]

def solve():
    for i in range(1,n+1):
        t = -1
        #求下轮最距离的点是哪个 这一步相当于heapsort 贪心
        for j in range(1,n+1):
            if not st[j] and(t == -1 or dist[t] > dist[j]):
                t = j
        st[t] = True
        for j in range(1,n+1):

            dist[j] = min(dist[j],dist[t] + graph[t][j])
            
    if dist[n] == float('inf'):
        return -1    
    else:
        return dist[n]
for i in range(m):
    x,y,z = map(int, input().split())
    graph[x][y] = min(graph[x][y], z)    # 处理重边：保留重边中权重最小的边
for i in range(1, n+1):    # 处理自环：正权边的自环一定不是最短路，所以初始化i到i的权重为0
    graph[i][i] = 0
 
st = [False]*(n+1)
dist = [float('inf')]*(n+1)
dist[1] = 0
print(solve())