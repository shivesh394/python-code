import math
n=int(input())
k=(1<<int(math.log2(abs(n)))+1)-1
print(k,n^k)