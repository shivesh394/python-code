def pal(s):
    s=s.split(" ")
    s="".join(s)
    if s==s[::-1]:
        return True
    else:
        return False

print(pal("never odd or even"))