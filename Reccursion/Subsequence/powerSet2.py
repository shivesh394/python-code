nums = [1,2,3,4]
nums.sort()
l = []
s = []
def dfs(ind):
    l.append(s.copy())
    for i in range(ind,len(nums)):
        s.append(nums[i])
        dfs(i+1)
        s.pop()

dfs(0)
print(l, len(l))

