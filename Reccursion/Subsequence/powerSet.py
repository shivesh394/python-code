s = '123'
l = []
subset = []
def powerSet(i):
    if i == len(s):
        l.append(subset.copy())
        return
    subset.append(s[i])
    powerSet(i+1)
    subset.pop()
    powerSet(i+1)

powerSet(0)
print(l)