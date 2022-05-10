#Write a Python program to check whether a given string is number or not using Lambda

str="99345"
check=lambda x:x.isnumeric()
print(check(str))