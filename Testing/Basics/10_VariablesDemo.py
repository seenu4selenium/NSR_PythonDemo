# Local Variables
# Global Variables

print("************************************")
# Local Variables
# Local variables are confined to their defined scope.
# In the following example, x and y are local variables:
def sum(x,y):
    sum = x + y
    return sum

print(sum(8,6))

print("************************************")
# Global Variables
# In contrast, a global variable is available throughout your entire code.
# Below is an example of a global variable, z:
z = 10

def afunction():
    global z
    print(z)

afunction()
print(z)

# Whether inside or outside a function, the global variable z is accessible.
# Moreover, you can modify a global variable within a function,
# impacting its value throughout the entire program:
z = 10

def afunction():
    global z
    z = 9

afunction()
print(z)
# After invoking afunction(), the value of the global variable changes for the entire program.
# Both local and global variables can coexist in a single Python program.
# Examine the following code and predict its output:
z = 10

def func1():
    global z
    z = 3

def func2(x,y):
    global z
    return x+y+z

func1()
total = func2(4,5)
print(total)
