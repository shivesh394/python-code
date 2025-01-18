def update(i, add):
    while i < n:
        fen[i] += add
        i += (i & (-i))
        
def sum(i):
    s = 0
    while i > 0:
        s += fen[i]
        i = i - (i & (-i));
    return s

def rangeSum(l, r):
    return sum(r) - sum(l - 1)

n = 10
nums = [23, 12, 9, 2, 1, 100, 3, 8, 92, 122]
fen = [0]*(n + 1)
for i in range(n):
    update(i + 1, nums[i])
    
print(rangeSum(4, 8))  #  1 base indexing
