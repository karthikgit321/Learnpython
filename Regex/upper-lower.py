#first character uppercase,contains lower case alphabets,only one digit allowed in between
import re

pattern='[A-Z][a-z]*[0-9][a-z]*'
#match=re.search(pattern,input("enter the alphanumeric word"))
#or
#match=re.match(pattern,input("enter the alphanumeric word"))
#or
match=re.findall(pattern,input("enter the alphanumeric word"))
if match:
    print("Valid match")
    print(match)
else:
    print("Invalid match")
    print(match)

