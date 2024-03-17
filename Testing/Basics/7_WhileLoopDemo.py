#Python While Loop
# Syntax of while loop
#     while condition:
#           body_of_while
num = 1
# loop will repeat itself as long as
# num < 10 remains true
while num < 10:
    print(num)
    #incrementing the value of num
    num = num + 3
print("******************************")
#Infinite while loop
# while True:
#    print("hello Srini, welcome")

# num = 1
# while num<5:
#    print(num)
print("******************************")
#Nested while loop in Python
i = 1
j = 5
while i < 4:
    while j < 8:
        print(i, ",", j)
        j = j + 1
        i = i + 1
print("******************************")
# Python – while loop with else block
num = 10
while num > 6:
   print(num)
   num = num-1
else:
   print("loop is finished")

print("******************************")
 # when else block will execute
number = int(input("Type any number: "))
flag = number % 2
if flag == 0:
    print("Given number is EVEN: ", number)
elif flag == 1:
    print("Given number is ODD: ", number)
else:
    print("Please enter valid int only")

