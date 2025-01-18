arr = [4,3,1,1,3,3,2]
from collections import Counter
count = Counter(arr)
import heapq
count = list(count.items())
heapq.heapify(count)
while count:
    print(heapq.heappop(count))