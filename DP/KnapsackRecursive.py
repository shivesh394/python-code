def Knapsack(wt,val,W,n):
    if(n==0 or W==0):
        return 0
    if(wt[n-1]<=W):
        return max(val[n-1]+Knapsack(wt,val,W-wt[n-1],n-1), Knapsack(wt,val,W,n-1))
    elif(wt[n-1]>W):
        return Knapsack(wt,val,W,n-1)


# n=int(input())
# wt=list(map(int,input().split()))
# val=list(map(int,input().split()))
# W=int(input())

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
x=Knapsack(wt,val,W,n)
print(x)
