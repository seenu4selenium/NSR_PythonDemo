#Control Statements
#IF, IF-ELSE, IF-ELIF-ELSE, NESTED-IF
#IF: syntax
# if condition:
#   block_of_code
flag = True
if flag==True:
    print("Welcome")
    print("To")
    print("NSRpython.com")
print("******************************")
flag = True
if flag:
    print("Welcome")
    print("To")
    print("NSRpython.com")
print("******************************")
flag = False
if flag:
    print("You Guys")
    print("are")
    print("Awesome")
print("******************************")
num = 100
if num < 200:
    print("num is less than 200")

print("###############################################################")
#IF-ELSE
# Python – Syntax of if..else statement
# if condition:
#    block_of_code_1
# else:
#    block_of_code_2
num = 22
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
print("###############################################################")
#Python If elif else statement example
# Syntax of if elif else statement in Python
# if condition:
#    block_of_code_1
# elif condition_2:
#    block_of_code_2
# elif condition_3:
#    block_of_code_3
# ..
# ..
# ..
# else:
#   block_of_code_n
num = 1122
if 9 < num < 99:
    print("Two digit number")
elif 99 < num < 999:
    print("Three digit number")
elif 999 < num < 9999:
    print("Four digit number")
else:
    print("number is <= 9 or >= 9999")

print("###############################################################")
#Python Nested If else statement
num = -99
if num > 0:
    print("Positive Number")
else:
    print("Negative Number")
    #nested if
    if -99<=num:
        print("Two digit Negative Number")