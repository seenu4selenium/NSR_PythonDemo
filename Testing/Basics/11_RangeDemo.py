# python range
# The range() function in Python is a versatile and commonly used function.
# It is designed to generate a sequence of numbers based on specified parameters.
# Syntax
# range(start, stop, step)

# Parameters:
# start: It denotes the starting value of the sequence. It’s optional, and the default value is 0.
# stop: Specifies the upper limit. The sequence does not include this number.
# step: The interval between numbers in the sequence. It’s optional with a default value of 1.

# Python range() Function
x = range(6)
for n in x:
  print(n)

print("***********************")
x = range(3, 20, 2)
for n in x:
  print(n)
