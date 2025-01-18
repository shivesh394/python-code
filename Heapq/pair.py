from heapq import heapify, heappush, heappop
heap = []  # This is min Heap
heapify(heap)
heappush(heap, [9, 0])
heappush(heap, [2, 7])
heappush(heap, [1, 9])
heappush(heap, [12, 2])
while heap:
    a, b = heappop(heap)
    print(a, b)