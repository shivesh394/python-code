#A tuple is a collection which is ordered and unchangeable.

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistuple))

thistuple = ("apple", "banana", "cherry", "apple", "cherry")  #Allow Duplicates
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")  #NOT a tuple
print(type(thistuple))

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])


x = ("apple", "banana", "cherry")
y = list(x)  #Convert the tuple into a list, change the list, and convert the list back into a tuple.
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")  
y = ("orange",)  #Add tuple to a tuple
thistuple += y
print(thistuple)

#You cannot remove items in a tuple.

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #this will raise an error because the tuple no longer exists

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 3
print(mytuple)
print(mytuple.count("apple"))
print(mytuple.index("apple"))
