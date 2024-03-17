# Python Arrays : Arrays are used to store multiple values in one single variable
# What is an Array?
# An array is a special variable, which can hold more than one value at a time.
# If you have a list of items (a list of car names, for example),
# storing the cars in single variables could look like this:

# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Get the value of the first array item:
x = cars[0]
print(x)

# Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

# Length
x = len(cars)
print(x)
print("**************************************************")
# Looping Array Elements
for x in cars:
  print(x)

print("**************************************************")
# Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

print("**************************************************")
# Removing Array Elements
#cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
# Delete the element that has the value "Volvo":
cars.remove("BMW")
print(cars)

# Array Methods
# Method	Description
# ======  ============
# append()	Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	    Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	    Sorts the list
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

names = ["Shashanka","Rupesh","Pandu"]
print(names)
names.append("Hari")
names.append("Jyothi")
names.append("Anitha")
print(names)
names.clear()
print(names)
print("//////////////////////////////////////")
names = ["Shashanka","Rupesh","Pandu"]
print(names)
names.append("Hari")
names.append("Jyothi")
names.append("Anitha")
print(names)
print(names.copy())
# names.count("Python")
# names.extend("Python")
print(names)
print(names.index("Pandu"))
print(names)
#sort
names.sort()
print(names)
#reverse the ArrayList
names.reverse()
print(names)
names.insert(4,"Viswa")
print(names)

