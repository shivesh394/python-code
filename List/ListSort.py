thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)  #for sort descending
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)



def myfunc(n):
      return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)  #Sort the list based on how close the number is to 50
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()  #sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)