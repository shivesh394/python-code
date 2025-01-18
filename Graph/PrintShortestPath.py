import heapq
dist = [float('inf')]*V
dist[S] = 0
parent = []
for i in range(V):
    parent.append(i)
heap = []
heapq.heappush(heap, [0, S])
while heap:
    dis, node = heapq.heappop(heap)
    for a in adj[node]:
        adjDis = a[1]
        adjNode = a[0]
        if dis + adjDis < dist[adjNode]:
            parent[adjDis] = node
            dist[adjNode] = dis + adjDis
            heapq.heappush(heap, [dis + adjDis, adjNode])
print(dist, parent)