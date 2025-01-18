# d is the number of characters in the input alphabet
d = 256

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    p = 0    # hash value for pattern
    t = 0    # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h * d) % q

    # Calculate the hash value of pattern and first window of text
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and pattern
        if p == t:
            # Check for characters one by one
            match = True
            for j in range(M):
                if txt[i + j] != pat[j]:
                    match = False
                    break
            if match:
                print(f"Pattern found at index {i}")

        # Calculate hash value for next window of text: Remove leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            # We might get negative value of t, converting it to positive
            if t < 0:
                t = t + q

# Driver code
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
q = 10**9 + 7  # A prime number
search(pat, txt, q)
