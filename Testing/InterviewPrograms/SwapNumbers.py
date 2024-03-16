#SWAP two number by using TEMP variable
print("SWAP two number by using TEMP variable")
number1 = int(input("Type any number: "))
number2 = int(input("Type any number: "))
print("Before swapping value for number1 is : ", number1) #10
print("Before swapping value for number2 is : ", number2) #20

# print("Swapping numbers using temp variable")
# temp = number1 #10
# number1 = number2 #20
# number2= temp #10
# print("After swapping value for number1 is : ", number1)
# print("After swapping value for number2 is : ", number2)

#SWAP two number without using TEMP variable
print("SWAP two number without using TEMP variable")
number1,number2 = number2, number1
print("After swapping value for number1 is : ", number1)
print("After swapping value for number2 is : ", number2)
