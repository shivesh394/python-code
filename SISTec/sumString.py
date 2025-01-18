n=input("Enter a number : ")
l=len(n)
sum=0
for i in range(0,l):
    sum=sum+int(n[i])
print("Sum : ",sum)