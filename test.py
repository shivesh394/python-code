def count_words(S):
    n = len(S)
    if n == 0:
        return 0
    

    dp[0] = 1  # There's 1 way to decode an empty string
    dp[1] = 1 if S[0] != '0' else 0  # Single character string must not start with '0'

    for i in range(2, n + 1):
        if '1' <= S[i-1] <= '9':
            dp[i] += dp[i-1]
        if '10' <= S[i-2:i] <= '26':
            dp[i] += dp[i-2]
    return dp[n]

if __name__ == "__main__":
    S = input("Enter the string: ").strip()
    n = len(S)
    dp = [0] * (n + 1)
    result = count_words(S)
    print(result, dp)
