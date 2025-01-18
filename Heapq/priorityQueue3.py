import heapq
h = []
heapq.heappush(h,(4, "Tom"))
heapq.heappush(h,(1, "Aruhi"))
heapq.heappush(h,(3, "Dyson"))
heapq.heappush(h,(2, "Bob"))

print(h)
print(h[0])
while h:
    print(heapq.heappop(h))