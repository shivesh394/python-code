nums = [1,2,3,1]
nums.sort()
l = []
s = []
def dfs(ind):
    l.append(s.copy())
    for i in range(ind,len(nums)):
        if i > ind and nums[i] == nums[i-1]:
            continue
        s.append(nums[i])
        dfs(i+1)
        s.pop()

dfs(0)
print(l, len(l))


# power set and subsequence are not same in case of duplicate elemenet