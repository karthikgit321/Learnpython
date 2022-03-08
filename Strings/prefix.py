def commonprefix(string1,string2):
    n1=len(string1)
    n2=len(string2)
    i=0
    j=0
    str=''
    while i<=n1-1 and j<=n2-1:
        if string1[i]!=string2[j]:
            break
        str+=string1[i]
        i+=1
        j+=1
    return str


def prefix1(arr,n):
    prefix=arr[0]
    for i in range(1,n):
        prefix=commonprefix(prefix,arr[i])
    return prefix

arr=['geeksforgeeks','geezer','geeks''gee']
n=len(arr)
compre=prefix1(arr,n)
print(compre)