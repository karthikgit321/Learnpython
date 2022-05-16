# arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
# new=[ele for ele in arr if arr[ele]!=0] + [y for y in arr if arr[y]==0]
# print(new)

str = 'geeksforgeeks'
num=int(input("Enter the number"))
l=[]
dict={}
for char in str:
    if char not in dict:
        dict[char]=1
    else:
        dict[char]+=1
print(dict)

for key,value in dict.items():
    if value==1:
        l.append(key)

print(l)
print(l[num-1])
