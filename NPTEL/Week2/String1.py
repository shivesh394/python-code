s1='Infi'
s2="Shivesh's wife"
s3='''"Sucku"'''
print(s1,s2,s3)
print(type(s1))

s4='''first
second'''  # multipe line string : only by using triple single quote
print(s4)

s="hello"
print("First :",s[0],s[-5])
print("Last :",s[4],s[-1])

t=s+" maxi"
print(t)

s5="BoomBaeBae"
print(len(s5))
print(s5[1:4])
print(s5[:4])
print(s5[1:])
print(s5[0:70])

s5=s5[0:0]+"aman"  #string is immutable
print(s5)