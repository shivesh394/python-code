arr = [0, 0, 1]
k = 1
arr = [1, 0, 8, 5, 1, 4]
k = sum(arr)
# arr = [1, 4, 4, 5]
# k = 5
n = len(arr)


dp = [[0]*(k + 1) for i in range(n)]
if arr[0] == 0:
    dp[0][0] = 2
else:
    dp[0][0] = 1

if arr[0] != 0 and arr[0] < k:
    dp[0][arr[0]] = 1
for i in range(1, n):
    for target in range(k + 1):
        notPick = dp[i - 1][target]
        pick = (dp[i - 1][target - arr[i]] if arr[i] <= target else 0)
        dp[i][target] = (notPick + pick) 

print(dp)