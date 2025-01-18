from collections import deque
V = 8
adj = [[], [2], [], [5], [], [], [3, 5], [3, 1]]

indegree = [0]*V
for i in range(V):
    for j in adj[i]:
        indegree[j] += 1
        
queue = deque()

for i in range(len(indegree)):
    if indegree[i] == 0:
        queue.append(i)
ans = []    
while queue:
    node = queue.popleft()
    ans.append(node)
    for i in adj[node]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)
            
print(ans)