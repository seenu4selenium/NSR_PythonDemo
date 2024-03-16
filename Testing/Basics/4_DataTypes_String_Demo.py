#Python Strings
# 1. How to create a String in Python
# ****************************************
# There are several ways to create strings in Python.
# 1. We can use ‘ (single quotes), see the string str in the following code.
# 2. We can use ” (double quotes), see the string str2 in the source code below.
# 3. Triple double quotes “”” and triple single quotes ”’ are used for creating multi-line strings in Python.

# lets see the ways to create strings in Python
str = 'NSR_Python'
print(str)

str2 = "Srinivas"
print(str2)

# multi-line string
str3 = """Welcome to 
   NSRpython.com"""
print(str3)

str4 = '''This is a NSR tech 
   blog'''
print(str4)

print("*************************************")
#2. How to access strings in Python
str = "Srini"

# displaying whole string
print(str)

# displaying first character of string
print(str[0])

# displaying third character of string
print(str[2])

# displaying the last character of the string
print(str[-1])

# displaying the second last char of string
print(str[-2])

print("*************************************")
#3. Python String Operations
#3.1. Getting a substring in Python – Slicing operation
str = "Welcome to NSR Python"

# displaying whole string
print("The original string is: ", str)

# slicing 10th to the last character
print("str[9:]: ", str[9:])

# slicing 3rd to 6th character
print("str[2:6]: ", str[2:6])

# slicing from start to the 9th character
print("str[:9]: ", str[:9])

# slicing from 10th to second last character
print("str[9:-1]: ", str[9:-1])

#3.2 Concatenation of strings in Python
str1 = "Hello"
str2 = "Srini"
str3 = "How are you?"

# Concatenation of three strings
print(str1 + str2 + str3)
print(str1+" "+ str2+" "+ str3)

#3.3 Repetition of string – Replication operator
#We can use * operator to repeat a string by specified number of times.
str = "ABC"
# repeating the string str by 3 times
print(str*3)
print((str+" ")*3)

#3.4 Python Membership Operators in Strings
# in: This checks whether a string is present in another string or not.
#      It returns true if the entire string is found else it returns false.
# not in: It works just opposite to what “in” operator does.
#         It returns true if the string is not found in the specified string else it returns false.
str = "Welcome to NSRpython.com"
str2 = "Welcome"
str3 = "Chaitanya"
str4 = "XYZ"

# str2 is in str? True
print(str2 in str)

# str3 is in str? False
print(str3 in str)

# str4 not in str? True
print(str4 not in str)

#3.5 Python – Relational Operators on Strings
# The relational operators works on strings based on the ASCII values of characters.
# The ASCII value of a is 97, b is 98 and so on.
# The ASCII value of A is 65, B is 66 and so on.
str = "ABC"
str2 = "aBC"
str3 = "XYZ"
str4 = "XYz"

# ASCII value of str2 is > str? True
print(str2 > str)

# ASCII value of str3 is > str4? False
print(str3 > str4)

