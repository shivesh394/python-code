def inf_sequence():
	num = 0
	while True:
		yield num
		num += 1
		
for i in inf_sequence():
	print(i, end=" ")
