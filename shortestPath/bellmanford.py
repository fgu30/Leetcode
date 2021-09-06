# https://www.acwing.com/problem/content/description/851/

n, m, k = map(int, input().split())
dist = [float('inf')] * (n + 1)
dist[1] = 0

tot_edges = [tuple(map(int, input().split())) for _ in range(m)]

for _ in range(k):
    pre_dist = list(dist)
    for a, b, w in tot_edges:
        dist[b] = min(dist[b], pre_dist[a] + w)

print('impossible') if dist[-1] == float('inf') else print(dist[-1])
