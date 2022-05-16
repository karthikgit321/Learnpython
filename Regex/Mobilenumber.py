#Mobile number --start with 8 or 9 and total digits 10
import re
pattern='[8-9][0-9]{9}'
match=re.findall(pattern,input("Enter the num"))
if match:
    print("its valid")
    print(match)
else:
    print("Not matching")
