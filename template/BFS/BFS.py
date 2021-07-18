#https://www.acwing.com/file_system/file/content/whole/index/content/2543808/


from collections import defaultdict

n,m = map(int,input().split())

graph = defaultdict(list)
d =[-1]*(n+1)
d[1] = 0

for row in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
dq = [1]
while dq:
    cur = dq.pop(0)
    for v in graph[cur]:
        if d[v] == -1:
            d[v] = d[cur] +1
            dq.append(v)
print(d[n])