# Python break Statement
# program to display all the elements before number 88
for num in [11, 9, 88, 10, 90, 3, 19]:
   print(num)
   if(num==88):
	   print("The number 88 is found")
	   print("Terminating the loop")
	   break

print("****************************************")
# Python Continue Statement
# program to display only odd numbers
for num in [20, 11, 9, 66, 4, 89, 44]:
    # Skipping the iteration when number is even
    if num%2 == 0:
        continue
    # This statement will be skipped for all even numbers
    print(num)

print("****************************************")
# Python pass Statement
for num in [20, 11, 9, 66, 4, 89, 44]:
    if num%2 == 0:
        pass
    else:
        print(num)