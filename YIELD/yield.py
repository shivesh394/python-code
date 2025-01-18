def fun_generator():
	yield "Hello world!!"
	yield "Geeksforgeeks"


obj = fun_generator()

print(type(obj))

print(next(obj))
print(next(obj))
