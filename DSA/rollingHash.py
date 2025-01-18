def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    d = 256
    i, j = 0, 0
    p = 0  
    t = 0  
    h = 1

    for i in range(M - 1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q 

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
            if j + 1 == M:
                print("Pattern found at index", i)
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q



txt = "GEEKS FOR GEEKSGEEK"
pat = "GEEK"
q = 101  
search(pat, txt, q)