a,b,c=[int(i) for i in input().split()] #list comprehension
max = a if a  >b and a > c else b if b > c else c
print(max)