V = 2
adj= [[[1, 9]], [[0, 9]]]
S = 0
from collections import deque
dist = [float('inf')]*V
dist[S] = 0
queue = deque()
queue.append([0, S])
while queue:
    dis, node = queue.popleft()
    for adjNode, adjDis in adj[node]:
        if dis + adjDis < dist[adjNode]:
            dist[adjNode] = dis + adjDis
            queue.append([dis + adjDis, adjNode])
print(dist)