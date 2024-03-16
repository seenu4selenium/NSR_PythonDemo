#Python List with examples
# 1. Create a List in Python
# list of floats
num_list = [11.22, 9.9, 78.34, 12.0]

# list of int, float and strings
mix_list = [1.13, 2, 5, "beginnersbook", 100, "hi"]

# an empty list
nodata_list = []
print("*********************************************")
#2. Accessing the items of a list
# a list of numbers
numbers = [11, 22, 33, 100, 200, 300]

# prints 11
print(numbers[0])

# prints 300
print(numbers[5])

# prints 22
print(numbers[1])
print("*********************************************")
#3. Negative Index to access the list items from the end
# a list of strings
my_list = ["hello", "Srini", "hi", "bye"]

# prints "bye"
print(my_list[-1])

# prints "world"
print(my_list[-3])

# prints "hello"
print(my_list[-4])

print("*********************************************")
#4. How to get a sublist in Python using slicing
# list of numbers
n_list = [1, 2, 3, 4, 5, 6, 7]

# list items from 2nd to 3rd
print(n_list[1:3])

# list items from beginning to 3rd
print(n_list[:3])

# list items from 4th to end of list
print(n_list[3:])

# Whole list
print(n_list[:])

print("*********************************************")
#5. List Operations
#5.1.Addition
# list of numbers
n_list = [1, 2, 3, 4]

# 1. adding item at the desired location
# adding element 100 at the fourth location
n_list.insert(3, 100)

# list: [1, 2, 3, 100, 4]
print(n_list)

# 2. adding element at the end of the list
n_list.append(99)

# list: [1, 2, 3, 100, 4, 99]
print(n_list)

# 3. adding several elements at the end of list
# the following statement can also be written like this:
# n_list + [11, 22]
n_list.extend([11, 22])

# list: [1, 2, 3, 100, 4, 99, 11, 22]
print(n_list)

#5.2 Update elements
# list of numbers
n_list = [1, 2, 3, 4]

# Changing the value of 3rd item
n_list[2] = 100

# list: [1, 2, 100, 4]
print(n_list)

# Changing the values of 2nd to fourth items
n_list[1:4] = [11, 22, 33]

# list: [1, 11, 22, 33]
print(n_list)

#5.3 Delete elements
# list of numbers
n_list = [1, 2, 3, 4, 5, 6]

# Deleting 2nd element
del n_list[1]

# list: [1, 3, 4, 5, 6]
print(n_list)

# Deleting elements from 3rd to 4th
del n_list[2:4]

# list: [1, 3, 6]
print(n_list)

# Deleting the whole list
del n_list

#5.4 Deleting elements using remove(), pop() and clear() methods
# remove(item): Removes specified item from list.
# pop(index): Removes the element from the given index.
# pop(): Removes the last element.
# clear(): Removes all the elements from the list.

# list of chars
ch_list = ['A', 'F', 'B', 'Z', 'O', 'L']

# Deleting the element with value 'B'
ch_list.remove('B')

# list: ['A', 'F', 'Z', 'O', 'L']
print(ch_list)

# Deleting 2nd element
ch_list.pop(1)

# list: ['A', 'Z', 'O', 'L']
print(ch_list)

# Deleting all the elements
ch_list.clear()

# list: []
print(ch_list)




