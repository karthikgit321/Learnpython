'''
a=input("Enter the string")
b=''

for char in a:
    if char not in b:
        b=b+char

print(b)
'''
'''
temp=list(input("Enter the string"))
print(temp)
New=[]
Prev=None
Prev1=None
for i in temp:
    if i!=Prev:
        New.append(i)
        Prev=i
        Prev1=None
    else:
        if Prev1=='+':
            continue
        else:
            New.append('+')
            Prev1='+'
print(' '.join(New))
'''
a=input("Enter the string")
b=''

for i in range(0,len(a)-1):
        if a not in b:
            if a[i]==a[i+1]:
                b=b+ "+"
            elif a[i] != a[i + 1]:
                b=b+a[i]
print(b)