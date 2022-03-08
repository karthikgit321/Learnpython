

import random

letters=['a','b','c','d','e','f','g','h']
numbers=['0','1','2','3','4','5']
symbols=['~','!','@','#','$','%','^','&']
#password=''
password_list=[]

print("Welcome to pypassword generator")
nr_letters=int(input("how many letter you want in your password\n"))
nr_numbers=int(input("how many numbers want in your password\n"))
nr_symbols=int(input("how many symbols you want in your password\n"))
'''
for i in range(0,nr_letters):
    b=random.choice(letters)
    password=password+b
print(str(password))

for i in range(0,nr_numbers):
    ran_no=random.choice(numbers)
    password=password+ran_no
print(password)

for i in range(0,nr_symbols):
    ran_symbol=random.choice(symbols)
    password=password+ran_symbol
print(password)

#password_generator=a+c+d
#print(password_generator)
#rand_pwd=random.choice(password_generator)
#print("The password generator has generated the below password\n",rand_pwd)
'''

for i in range(0,nr_letters):
    b=random.choice(letters)
    password_list.append(b)
print(password_list)

for i in range(0,nr_numbers):
    ran_no=random.choice(numbers)
    password_list.append(ran_no)
print(password_list)

for i in range(0,nr_symbols):
    ran_symbol=random.choice(symbols)
    password_list.append(ran_symbol)
print(password_list)

random.shuffle(password_list)
password=''
for i in password_list:
    password=password+i
print(password)