for s in[*open(0)][1:]:
    a,b,c=map(int,s.split())
    print(a^b^c)
