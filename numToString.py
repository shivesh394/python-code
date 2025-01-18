n = input()
s = ""
for i in n:
    s += chr(int(i) + 64)
str = ''.join(sorted(s))
print(str)