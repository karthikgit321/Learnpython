

list2=[]
list3=[]

#1. Move all ZERO to end
#2. Move all ZERO to index 3
list1=[1,2,3,0,0,0,0,0,0,4,5,6,7,8]
l=len(list1)
for i in range(0,l):
    if list1[i]==0:
        list2.append(list1[i])
    else:
        list3.append(list1[i])

print(list2)
print(list3)

for i in range(0,len(list2)):
    list3.insert(list2[i])
print(list3)


#list2 contains all zero's
'''
def pushzeros(arr,n):
    count=0

    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count=count+1
    print(arr)
    while count < n:
        arr[count] = 0
        count += 1

arr=[0,0,0,0,1,2,3,4,5,0,0,0]
n=len(arr)
pushzeros(arr,n)
print(arr)
'''