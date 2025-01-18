def fun(i, target):
    if target == 0: 
        return True
    if i == 0: 
        return arr[i] == target
    if dp[i][target] != -1:
        return dp[i][target]
    dp[i][target] = fun(i - 1, target) or (fun(i - 1, target - arr[i]) if arr[i] <= target else False)
    return dp[i][target]
dp = [[-1]*(k + 1) for i in range(len(arr))]
ans = fun(n - 1, k)
print(ans)
print(dp)