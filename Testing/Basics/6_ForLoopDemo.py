#Python for Loop
#Syntax of For loop in Python
# for <variable> in <sequence>:
   # body_of_loop that has set of statements
   # which requires repeated execution
# List of integer numbers
numbers = [1, 2, 4, 6, 11, 20]

# variable to store the square of each num temporary
sq = 0

# iterating over the given list
for val in numbers:
    # calculating square of each number
    sq = val * val
    # displaying the squares
    print(sq)
print("*******************************************************")
#Python for loop example using range() function
# Program to print the sum of first 5 natural numbers
# variable to store the sum
sum = 0

# iterating over natural numbers using range()
for val in range(1, 6):
    # calculating sum
    sum = sum + val

# displaying sum of first 5 natural numbers
print(sum)

print("*******************************************************")
#For loop with else block
for val in range(5):
	print(val)
else:
	print("The loop has completed execution")

print("*******************************************************")
#Nested For loop in Python
for num1 in range(3):
	for num2 in range(10, 14):
		print(num1, ",", num2)
