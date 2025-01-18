def build(ind, low, high):
    if low == high:
        seg[ind] = nums[low]
        return
    mid = (low + high) // 2
    build(2 * ind + 1, low, mid)
    build(2 * ind + 2, mid + 1, high)
    seg[ind] = seg[2 * ind + 1] + seg[2 * ind + 2]
    
def querySumLazy(ind, low, high):
    if lazy[ind] != 0:
        seg[ind] += (high - low + 1) * lazy[ind]
        if low != high:
            lazy[2 * ind + 1] += lazy[ind]
            lazy[2 * ind + 2] += lazy[ind]
        lazy[ind] = 0
        
    if r < low or l > high or low > high:
        return 0
    
    if l <= low and r >= high:
        return seg[ind]
        
    mid = (low + high) // 2
    return querySumLazy(2 * ind + 1, low, mid) + querySumLazy(2 * ind + 2, mid + 1, high)

def rangeUpdate(ind, low, high):
    if lazy[ind] != 0:
        seg[ind] += (high - low + 1) * lazy[ind]
        if low != high:
            lazy[2 * ind + 1] += lazy[ind]
            lazy[2 * ind + 2] += lazy[ind]
        lazy[ind] = 0
    
    if r < low or l > high or low > high:
        return
    
    if l <= low and r >= high:
        seg[ind] += (high - low + 1) * val
        if low != high:
            lazy[2 * ind + 1] += val
            lazy[2 * ind + 2] += val
        return
    
    mid = (low + high) // 2
    rangeUpdate(2 * ind + 1, low, mid)
    rangeUpdate(2 * ind + 2, mid + 1, high)
    seg[ind] = seg[2 * ind + 1] + seg[2 * ind + 2]
        
    
n = 10
nums = [23, 12, 9, 2, 1, 100, 3, 8, 92, 122]
l, r, val = 3, 7, 100
seg = [0] * (4*n)
lazy = [0] * (4*n)
build(0, 0, n - 1)
rangeUpdate(0, 0, n - 1)
print(querySumLazy(0, 0, n - 1))
