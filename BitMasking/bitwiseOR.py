def bit(s):
    s1=''
    for i in range(len(s[0])):
        s1+=str(int(s[0][i]) or int(s[1][i]))
    return s1

l=["1001011","1100001"]
print(bit(l))