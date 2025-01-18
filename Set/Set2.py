# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is ordered* and changeable. No duplicate members.

s1={1,2,3,4,5}
print(s1)
s2={"maxi","belly","bae"}
print(s2)
s3={True,False}
print(s3)
s4={1,"hi",1.3}
print(s4)

s5=set((1,2,3,4))
print(s5)
print(type(s5))

thisset = {"apple", "banana", "cherry"}
print(thisset)

for x in thisset:
  print(x)

print("banana" in thisset)

thisset.add("orange")
print(thisset)

tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset.remove("banana")  #If the item to remove does not exist, remove() will raise an error.
print(thisset)

thisset.discard("banana")  #If the item to remove does not exist, discard() will NOT raise an error.
print(thisset)    

x = thisset.pop()  #Sets are unordered, so when using the pop() method, you do not know which item that gets removed
print(x)
print(thisset)

thisset.clear()  #The clear() method empties the set
print(thisset)

del thisset  #The del keyword will delete the set completely
print(thisset)