l=[[  0 for _ in range(51)] for _ in range(4)]
def Knapsack(wt,val,W,n):
    for i in range(n+1):
        for j in range(W+1):
            if(i==0 or j==0): 
                l[i][j]=0  
            elif(wt[i-1]<=j):
                l[i][j]=max(val[i-1]+l[i-1][j-wt[i-1]], l[i-1][j])
            else:
                l[i][j]=l[i-1][j]
    return l[n][W]

# n=int(input())
# wt=list(map(int,input().split()))
# val=list(map(int,input().split()))
# W=int(input())

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print(Knapsack(wt,val,W,n))
