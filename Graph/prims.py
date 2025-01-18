from heapq import heappush, heappop
V = 3
edges = [[0, 1, 5], [1, 2, 3], [0, 2, 1]]
adj = [[] for _ in range(V)]
for u, v, wt in edges:
    adj[u].append([v, wt])
    adj[v].append([u, wt])
vis = [0]*V
minHeap = []
heappush(minHeap, [0, 0, -1])
ans = 0
while minHeap:
    cost, node, parent = heappop(minHeap)
    if not vis[node]:
        ans += cost
        vis[node] = 1
        for adjNode, adjCost in adj[node]:
            heappush(minHeap, [adjCost, adjNode, node])
            
print(ans)