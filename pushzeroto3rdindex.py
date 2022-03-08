

def pushzeros(arr,n):
    l1=[]
    l2=[]
    for i in range(n):
        if arr[i]==0:
            l1.append(arr[i])
        else:
            l2.append(arr[i])
    print(l1)
    print(l2)

    for i in range(0,len(l1)):
        l2.insert(3,l1[i])
    print(l2)





'''
def pushzeros(arr,n):
    count=0
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    print(arr)
    while (count<n):
        arr[count]=0
        count+=1
       
    print(arr)
'''

arr=[0,0,1,2,3,4,0,5,0,6,7,8,0,0,9,0]
n=len(arr)
pushzeros(arr,n)
