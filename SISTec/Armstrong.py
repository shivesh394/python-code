num=input("Enter a number :")
n=len(num)
sum=0
temp=int(num)
while temp>0:
    digit=temp%10
    sum=sum+digit**n
    temp//=10

if int(num)==sum:
    print("Number is Armstrong number")
else:
    print("Number is not Armstrong number")