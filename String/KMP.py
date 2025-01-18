text = 'aacaaabaaacaaaa'
n = len(test)
pat = 'aaacaaaa'
m = len(pat)
lps = [0]*m

def ComputePrefix():
    preLPS, i = 0, 1
    while i < m:
        if pat[i] == pat[preLPS]:
            preLPS += 1
            lps[i] = preLPS
            i += 1
        elif preLPS == 0:
            lps[i] = 0
            i += 1
        else:
            preLPS = lps[preLPS - 1]

def stringMatching():
    ComputePrefix()
    i, j = 0, 0
    while i < n:
        if text[i] == pat[j]:
            i, j = i + 1, j + 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == m:
            print('Match')
            break

stringMatching()