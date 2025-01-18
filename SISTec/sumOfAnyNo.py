def sum(*n):
    print(type(n))
    total=0
    for i in n:
        total+=i
    print("sum :",total)

sum(1,2,3,4,5,6,7)
sum(1,2)
sum(23,78)


# There is no function overloading concept in python