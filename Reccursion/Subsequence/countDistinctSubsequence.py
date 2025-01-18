def fun(s: str) -> int:
    n = len(s)
    count = 1
    m1 = {}
    for i in range(n):
        if s[i] not in m1:
            m1[s[i]] = count
            count *= 2
        else:
            temp = m1[s[i]]
            m1[s[i]] = count
            count *= 2
            count -= temp
    return count

# print(fun('asdfgfd'))
print(fun('1231'))


# power set and subsequence are not same in case of duplicate elemenet
