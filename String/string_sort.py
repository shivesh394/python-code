# leetcode 179
from functools import cmp_to_key
nums = [3,30,34,5,9]
nums_str = [str(num) for num in nums]
def fun(n1, n2):
    if n1 + n2 > n2 + n1:
        return -1
    else:
        return 1
nums_str.sort(key = cmp_to_key(fun))
print(nums_str)