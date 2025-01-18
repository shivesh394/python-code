def build(ind, low, high):
    if low == high:
        seg[ind] = nums[low]
        return
    mid = (low + high) // 2
    build(2 * ind + 1, low, mid)
    build(2 * ind + 2, mid + 1, high)
    seg[ind] = seg[2 * ind + 1] + seg[2 * ind + 2]

def query(ind, low, high):
    if l <= low and r >= high:
        return seg[ind]
    if l > high or r < low:
        return 0
    mid = (low + high) // 2
    left = query(2 * ind + 1, low, mid)
    right = query(2 * ind + 2, mid + 1, high)
    return left + right
    
def pointUpdate(ind, low, high):
    if low == high:
        seg[ind] += val
        return
        
    mid = (low + high) // 2
    if node <= mid:
        pointUpdate(2 * ind + 1, low, mid)
    else:
        pointUpdate(2 * ind + 2, mid + 1, high)
    seg[ind] = seg[2 * ind + 1] + seg[2 * ind + 2]
    
n = 10
nums = [23, 12, 9, 2, 1, 100, 3, 8, 92, 122]
l, r, node, val = 3, 7, 5, 100
seg = [0] * (4*n)
build(0, 0, n - 1)
pointUpdate(0, 0, n - 1)
print(query(0, 0, n - 1))