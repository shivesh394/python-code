l=[12,3,4,56,23,4,25,90,67,5]

if l[0]>l[1]:
    lar=l[0]
    sec=l[1]
else:
    lar=l[1]
    sec=l[0]
    
for i in range(2,len(l)):
    if l[i]>lar:
        sec=lar
        lar=l[i]
        
    elif(l[i]>sec):
        sec=l[i]

print(lar,sec)