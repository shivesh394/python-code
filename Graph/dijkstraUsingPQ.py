V = 3
adj = [[[1, 10], [2, 15]], [], [[1, -6]]]
S = 0


import heapq
dist = [float('inf')]*V
dist[S] = 0
heap = []
heapq.heappush(heap, [0, S])
while heap:
    dis, node = heapq.heappop(heap)
    for adjNode, adjDis in adj[node]:
        if dis + adjDis < dist[adjNode]:
            dist[adjNode] = dis + adjDis
            heapq.heappush(heap, [dis + adjDis, adjNode])
print(dist)