l1=[6,4,3,1,2]
n=int(input("enter the number of positions"))
print(l1[-n:])
rotated_list=l1[-n:]+l1[:-n]
print(rotated_list)
