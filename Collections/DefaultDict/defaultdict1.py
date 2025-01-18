from collections import defaultdict
d = defaultdict(lambda : "not present")
d["a"] = 1
d["b"] = 2
print(d)
print(d['c'])