n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
l=student_marks[query_name]
a=0
s=0
for i in l:
    s=s+i
a=float(s/float(len(l)))
res = "{:.2f}".format(a)
print(res) 


# input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika


# Sample Output 
# 56.00