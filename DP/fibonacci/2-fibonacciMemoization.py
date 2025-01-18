def fib(n):
    if n <= 1:
        return n 
    if dp[n] != -1:
        return dp[n]
    dp[n] = fib(n - 1) + fib(n - 2)
    return dp[n]
n = 10
dp = [-1]*(n + 1)
print(fib(n))
print(dp)


# TC - O(n)
# SC - O(n)