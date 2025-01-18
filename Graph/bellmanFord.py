V = 3
edges = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
S = 2

dist = [float('inf')]*V
dist[S] = 0
for i in range(V - 1):
    for u, v, wt in edges:
        if dist[u] + wt < dist[v]:
            dist[v] = dist[u] + wt

for u, v, wt in edges:
    if dist[u] + wt < dist[v]:
        print('Negative Cycle')

print(dist)