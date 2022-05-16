import re
pattern=r'([A-Za-z0-9])\1'
match=re.search(pattern,input("enter the alphanumeric"))
print(match)