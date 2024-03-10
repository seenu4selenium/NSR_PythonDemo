number = int(input("Type any number: "))

flag = number % 2
if flag ==0:
    print("Given number is EVEN: ", number)
elif flag ==1:
    print("Given number is ODD: ", number)
else:
    print("Please enter valid int only")
