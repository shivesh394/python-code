s = '12345'
base = 1
num = 0
num1 = 0
for i in range(len(s)):
    num += int(s[i])*base
    base *= 10
    num1 = num1*10 + int(s[i])

print(num,num1)