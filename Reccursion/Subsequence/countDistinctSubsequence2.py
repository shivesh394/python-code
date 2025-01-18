def fun(s):
    n = len(s)
    last = [0]*26
    dp = [-1]*(n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        idx = ord(s[i - 1]) - ord('1')
        j = last[idx]
        dup = dp[j - 1] if j > 0 else 0
        dp[i] = 2*dp[i - 1] - dup
        last[idx] = i
    return (dp[n] - 1) 

# print(fun('asdfgfd'))
print(fun('1231'))



# power set and subsequence are not same in case of duplicate elemenet