arr = [0, 0, 1]
k = 1
# arr = [1, 0, 8, 5, 1, 4]
# k = 2
n = len(arr)
def fun(i, k):
    if i == 0 :
        if k == 0 and arr[i] == 0:
            dp[i][k] = 2
            return dp[i][k]
        if k == 0 or arr[i] == k:
            dp[i][k] = 1
            return dp[i][k]
        dp[i][k] = 0
        return dp[i][k]
    if dp[i][k] != -1:
        return dp[i][k]
    notPick = fun(i - 1, k)
    pick = fun(i - 1, k - arr[i]) if arr[i] <= k else 0
    dp[i][k] = notPick + pick
    return dp[i][k]
dp = [[-1]*(k + 1) for i in range(n)]
fun(n - 1, k)
print(dp)