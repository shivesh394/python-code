def search(pat, txt, MOD):
    M = len(pat)
    N = len(txt)
    p = 0    
    t = 0    
    h = 1
    d = 256

    for i in range(M - 1):
        h = (h * d) % MOD

    for i in range(M):
        p = (d * p + ord(pat[i])) % MOD
        t = (d * t + ord(txt[i])) % MOD

    for i in range(N - M + 1):
        if p == t:
            print(f"Pattern found at index {i}")

        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % MOD   # ((G * 256 ^ 3 + E * 256 ^ 2 + E * 256 ^ 1 + K * 256 ^ 0) - G * h) * d + S   for i = 0



txt = "GEEKS FOR GEEKS"
pat = "GEEK"
MOD = 10**9 + 7  
search(pat, txt, MOD)