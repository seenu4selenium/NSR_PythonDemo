# Python Functions
# Why use function in Python?
# a function is a block of code that performs a specific task.
# 1. Code re-usability
# 2. Improves Readability
# 3. Avoid redundancy

# Syntax of functions in Python
# def function_name(function_parameters):
# 	function_body # Set of Python statements
#         return # optional return statement
def add(num1, num2):
    return num1 + num2


sum1 = add(100, 200)
sum2 = add(8, 9)
print(sum1)
print(sum2)
print("*****************************************")
# Default arguments in Function
# default argument for second parameter
def add(num1, num2=1):
    return num1 + num2


sum1 = add(100, 200)
sum2 = add(8)  # used default argument for second param
sum3 = add(100)  # used default argument for second param
print(sum1)
print(sum2)
print(sum3)

print("*****************************************")
# Python Recursion
# A function is said to be a recursive if it calls itself.
# For example, lets say we have a function abc() and in the body of abc() there is a call to the abc().
# Example of recursion in Python to
# find the factorial of a given number

def factorial(num):
    """This function calls itself to find
    the factorial of a number"""

    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

num = 5
print("Factorial of", num, "is: ", factorial(num))

