def my_function(a,b,c):
      print("The youngest child is " + a)

my_function("Emil", "Tobias", "Linus")   #Position argument


# def my_function(add="clg",name):  #default argument at last
#       print(name,"and",add)


def my_function(name, add="clg"):
      print(name,"and",add)

my_function("Rahul")    #default agrument
my_function("Rahul",add="bhs")      


def my_function(*kids):
      print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")     #Arbitrary Arguments, *args -->normal variable length arguments -->tuple


def my_function(child3, child2, child1):
      print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")   #Keyword Arguments,kwargs


def my_function(**kid):
      print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")  #Arbitrary Keyword Arguments, **kwargs  -->keyword variable length arguments -->dictionary


def my_function(food):
      for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)


def myfunction():
  pass