l1=[(1,2,3),(4,5),(6,7,8,9),(1 ,)]
l2=''
l3=[]
l4=[]
count=0
'''
for i in range(len(l1)):
    l2=len(l1[i])
    print(type(l2))
    l3.append(l2)
    print(type(l3))
print(l3)

for i in range(len(l1)):
    l4.extend(l1[i]*l3[i])
print(l4)

'''

for i in[j for j in l1]:
    print((i*len(i)))




