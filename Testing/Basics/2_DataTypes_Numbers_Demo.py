#Python Numbers
# int
num = 100
print("type of num: ",type(num))

# float
num2 = 10.99
print("type of num2: ",type(num2))

# complex numbers
num3 = 3 + 4j
print("type of num3: ",type(num3))
print("********************************")
x = int(input("Enter x:"))
y = int(input("Enter y:"))

result = x + y
print(result)

print("********************************")
num = 100
# true because num is an integer
print(isinstance(num, int))

# false because num is not a float
print(isinstance(num, float))

# false because num is not a complex number
print(isinstance(num, complex))