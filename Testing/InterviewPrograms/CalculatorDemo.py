print("Calculator*********")
number1 = int(input("Type any number: "))
number2 = int(input("Type any number: "))

print("Enter operation would you like to perform?")
ch = input("Enter which operation would you like to perform: +, -, *, / : ")
result = 0

if ch == '+':
    result = number1+number2
elif ch == '-':
    result = number1-number2
elif ch == '*':
    result = number1*number2
elif ch == '/':
    result = number1/number2
print(number1, ch, number2, ":" , result)
