#https://www.acwing.com/problem/content/description/852/

import collections, heapq
n, m = map(int, input().split())

## 初始化， g代表邻接表， 里面存出的元素是[d,v] d代表距离， v代表点
g = collections.defaultdict(list)

## st代表是否访问
st = [False for i in range(n+1)]

## 记录当前最短距离
dist = [float("inf") for i in range(n+1)]

## 优先队列
h = []

##初始化起点距离为0 并放入队列
dist[1] = 0
heapq.heappush(h, [0, 1])

## 读入边的信息， 注意存储格式
for i in range(m):
    a, b, c = map(int, input().split())
    g[a].append([c, b])

## 堆优化的dijkstra 复杂度 O(mlogm)
def dijkstraWithHeap():    
    while len(h) != 0:
        d, v = heapq.heappop(h)
        if st[v]:
            continue
        st[v] = True
        for d, j in g[v]:
            if dist[j] > dist[v] + d:
                dist[j] = dist[v] + d
                heapq.heappush(h, [dist[j], j])

dijkstraWithHeap()
print(dist[n] if dist[n] != float("inf") else -1)