def dis(**kwrgs):
    print(type(kwrgs))
    print(kwrgs)
    for i,j in kwrgs.items():
        print(i,j)

dis(a="abc",x="xyz")