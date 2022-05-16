l=(input("Enter the list"))
list1=[]

for i in range(len(l),0,-1):
    if l[i-1] not in list1:
        list1.append(l[i-1])
print(list1)
print(type(list1))




