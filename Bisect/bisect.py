import bisect

li = [1, 3, 4, 4, 4, 6, 7]


print ("Rightmost index to insert, so list remains sorted is : ",end="")
print (bisect.bisect(li, 4))

# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print ("Leftmost index to insert, so list remains sorted is : ", end="")
print (bisect.bisect_left(li, 4))

# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print ("Rightmost index to insert, so list remains sorted is : ",end="")
print (bisect.bisect_right(li, 4))
