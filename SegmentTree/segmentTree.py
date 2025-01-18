
def build(ind, low, high):
    if low == high:
        seg[ind] = nums[low]
        return
    mid = (low + high) // 2
    build(2 * ind + 1, low, mid)
    build(2 * ind + 2, mid + 1, high)
    seg[ind] = max(seg[2 * ind + 1], seg[2 * ind + 2])

def query(ind, low, high, l, r):
    if l <= low and r >= high:
        return seg[ind]
    if l > high or r < low:
        return -float('inf')
    mid = (low + high) // 2
    left = query(2 * ind + 1, low, mid, l, r)
    right = query(2 * ind + 2, mid + 1, high, l, r)
    return max(left, right)
    
n = 10
nums = [23, 12, 9, 2, 1, 100, 3, 8, 92, 122]
seg = [0] * (4*n)
build(0, 0, n - 1)
print(query(0, 0, n - 1, 3, 7))