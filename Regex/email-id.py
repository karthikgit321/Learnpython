import re
#karthi10ece@gmail.com
pattern='[a-zA-z0-9_\-\.]+[@][a-z]+[\.][a-z]{2,3}'

match=re.match(pattern,input("Enter the email id"))
if match:
    print("valid Email")
else:
    print("Invalid Email")
print(match.group(1))