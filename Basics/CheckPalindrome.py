# check any permutation is palindrome or not

s='1123121345'
l=[]
l1=[]
for i in s:
    if i not in l1:
        l1.append(i)
        l.append(s.count(i))

count1=0
count2=0
for i in l:
    if(i%2==0):
        count1+=1
    else:
        count2+=1
    

if(count1==len(l)):
    print("YES")
elif(count1==len(l)-1 and count2==1):
    print("YES")
else:
    print("NO")


# count = Counter(s)
# print(count) 
# res = 0
# for c in count.values():
#     if c % 2 != 0:
#         res += 1
#         if res > 1:
#             print('Not')
# if res <= 1:
#     print('Palindrome')