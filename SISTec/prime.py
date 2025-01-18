from math import sqrt
n=int(input("Enter a number : "))
a=0
if n>1:
    # for i in range(2,int(n**0.5)+1):
    for i in range(2,int(sqrt(n))+1):
        if(n%i == 0):
            a = 1
            print("Not Prime")
            break

    if a == 0:
        print("Prime")