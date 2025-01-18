# Example 3: Accessing Items in a deque
# index(ele, beg, end):- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.
# remove(): This function removes the first occurrence of the value mentioned in arguments.
# count(): This function counts the number of occurrences of value mentioned in arguments.


import collections

de = collections.deque([1, 2, 3, 3, 4, 2, 4])

# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print (de.index(4,2,5))

# using count() to count the occurrences of 3
print("The count of 3 in deque is : ", de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)
print(de)
