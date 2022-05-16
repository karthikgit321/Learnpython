l=[1,2,3,4,5,5,6,6]


d={}
for i in l:
    d[i]=l.count(i)
print(d)
count=0
for key,value in d.items():
    if value>1:
        count+=1
print(count)