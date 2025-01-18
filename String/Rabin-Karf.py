# leetcode 214
# 214. Shortest Palindrome
# You are given a string s. You can convert s to a palindrome by adding characters in front of it.
# Return the shortest palindrome you can find by performing this transformation.

prefix = 0
suffix = 0
base = 29
last_ind = 0
power = 1
mod = 10**9 + 7

for i, c in enumerate(s):
    char = (ord(c) - ord('a') + 1)
    prefix = (prefix * base + char) % mod

    suffix = (suffix + char * power) % mod
    power = (power * base) % mod

    if prefix == suffix:
        last_ind = i

suffix = s[last_ind + 1 :]
return suffix[::-1] + s