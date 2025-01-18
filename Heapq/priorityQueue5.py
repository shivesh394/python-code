import heapq
h = [[2, 5], [1, 200], [7, 4], [1, 4], [5, 8], [1, 100]]
# h = [[2, 5], [1, 200, 400], [7, 4], [1, 4], [5, 8], [1, 100]]
# h = [5, 4, 3, 2, 1]
# h = {5 : 1, 4 : 2, 3 : 3, 2 : 4, 1 : 5}
# h = list(h.items())
heapq.heapify(h)
print(h)
while h:
    # print(heapq.heappop(h))
    a, b = heapq.heappop(h)
    print(a, b)