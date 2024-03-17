# Python Random Module

# import random
from random import random

# Prints random item
print(random())
print("*********************************")
#another way
import random
# Prints random item
print(random.random())

print("*********************************")
from random import random
lst = []
for i in range(10):
    lst.append(random())
# Prints random items
print(lst)

print("*********************************")
#Python Random seed() Method
import random

random.seed(10)
print(random.random())
#Printing the random number twice
random.seed(10)
print(random.random())



print("*****************************************")
#print random email id's
import random
import string

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Generate and print 10 random email-like strings
for _ in range(10):
    print(generate_random_email())



