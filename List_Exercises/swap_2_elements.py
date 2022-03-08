'''
list=[1,2,3,4,5]
print(list)
list[0],list[3]=list[3],list[0]
print(list)
'''


def swap(list):
    pos1=int(input("Enter the pos1\n"))
    pos2=int(input("Enter the pos2\n"))
    first_ele=list.pop(pos1)
    sec_ele=list.pop(pos2-1)
    list.insert(pos1,sec_ele)
    list.insert(pos2,first_ele)
    return list




list=[1,2,3,4,5]
print(swap(list))






