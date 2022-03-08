list=(input("Enter the list").split())
for i in range(0,len(list)):
    list[i]=int(list[i])
print (list)

def interchange():
    l1=[]
    l2=[]
    l1=list.pop()
    print(l1)
    print(list)
    l2=list.pop(0)
    print(l2)
    list.append(l2)
    print(list)
    list[0]=l1
    print(list)
#interchange()
#OR

def first_list():
    temp=list[-1]
    list[-1]=list[0]
    list[0]=temp
    print(list)

first_list()

