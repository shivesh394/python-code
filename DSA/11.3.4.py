# Problem statement
# There are given n ropes of different lengths, we need to connect these ropes into one rope. 
# The cost to connect two ropes is equal to sum of their lengths. 
# We need to connect the ropes with minimum cost.

import heapq

def maxCost(nums):
    heapq.heapify(nums)
    ans = 0
    while nums:
        a = heapq.heappop(nums)
        if nums:
            b = heapq.heappop(nums)
            ans += a + b
            heapq.heappush(nums, a + b)
        else:
            return ans



nums = [4, 3, 2, 6]
print(maxCost(nums))