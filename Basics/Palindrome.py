n=123321
s=str(n)
count=0
j=len(s)-1
for i in range(len(s)//2):
    if s[i]==s[j]:
        count+=1
    j-=1
    
if(count==len(s)//2):
    print("palimdrome")
else:
    print("not")