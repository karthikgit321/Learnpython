str="hello welcome to python"

l=str.split()
a=[]
print(l)

for count, ele in enumerate(l):
    print(count)
    print(ele)
    if count==0 or count==2:
        a.append(ele[::-1])
    else:
        a.append(ele.capitalize())
print(a)
print(' '.join(a))