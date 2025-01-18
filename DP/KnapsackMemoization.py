l=[[-1 for _ in range(51)] for _ in range(4)]
def Knapsack(wt,val,W,n):
    if(n==0 or W==0):
        return 0
    if(l[n][W]!=-1):
        return l[n][W]
    if(wt[n-1]<=W):
        l[n][W]=max(val[n-1]+Knapsack(wt,val,W-wt[n-1],n-1), Knapsack(wt,val,W,n-1))
        return l[n][W]
    elif(wt[n-1]>W):
        l[n][W]=Knapsack(wt,val,W,n-1)
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
