import datetime

f = open("C:\\Users\\nalla\\OneDrive\\Desktop\\shashanka.txt","r")
lines = f.readlines()
print(lines)
print("********************************")
#Reading a file Line-By-Line
for abc in lines:
    print(abc,end="")

# print("********************************")
# for abc in lines:
#     abc.replace("\n","")
#     print(abc)

print("//////////////////////////////////////////////////////")

#with keyword
filePath ="C:\\Users\\nalla\\OneDrive\\Desktop\\shashanka.txt"
with open(filePath) as f:
    abc = f.read().splitlines()

for lines in abc:
    print(lines)

print("Write the file //////////////////////////////////////////////////////")
#generate the unique timeStamp
now = datetime.datetime.now()
timeStamp = now.strftime("%Y%m%d_%H%M%S")
# shashanka20240316_213800.txt
filePath ="C:\\Users\\nalla\\OneDrive\\Desktop\\shashanka"+timeStamp+".txt"
abcd = open(filePath,'w')
abcd.write("Python is scripting Language, sdgshsfdhdfhdfhTEST")
abcd.close()








