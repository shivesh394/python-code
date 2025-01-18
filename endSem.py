n = int(input())
l = []
for i in range(n):
    temp = list(map(str, input().split()))
    l.append(temp)
import heapq
heapq.heapify(l)
while l:
    a, b = heapq.heappop(l)[1:]
    print(a, b)
