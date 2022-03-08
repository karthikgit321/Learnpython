a=input("enter the string1")
b=input("enter the string2")
count=0
for i in range(0,len(min(a,b))):
    if (a[i:i+2]==b[i:i+2]):
        count=count+1
print(count)