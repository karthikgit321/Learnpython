l=[1,10,12,15,18]
element=int(input("Enter the number to be searched"))
'''
if element in l:
    print("Element exists")
else:
    print("Element doesn't exists")
'''
k=l.count(element)
if k>0:
    print("Element exists")
else:
    print("Element doesnt exists")