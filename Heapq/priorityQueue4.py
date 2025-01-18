from heapq import heapify, heappush, heappop
heap = []  # This is min Heap
heapify(heap)
heappush(heap, 9)
heappush(heap, 40)
heappush(heap, 30)
heappush(heap, 50)

print(heap)
print(heappop(heap))
print(heap)
