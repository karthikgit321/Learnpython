# a=[1,2,3,4,5,6]
# b=['a','b','c','d','e','f','g']
# dict ={}
#
# '''
# for x in range(len(l1)):
#     dict[l2[x]] = l1[x]
# print(dict)
# '''
# def list_to_dict1(a,b):
#     temp = {}
#     len_a = len(a)
#     len_b = len(b)
#     i =  j = 0
#     while i<len_a and j<len_b:
#         temp[a[i]] = b[j]
#         i += 1
#         j += 1
#
#     while i< len_a:
#         temp[a[i]] = None
#         i += 1
#
#     while j<len_b:
#         temp[b[j]] = None
#         j += 1
#
#     print(temp)
#
# list_to_dict1(a,b)

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
s3={}

a=len(set1)
b=len(set2)
for i in set1:
    for j in set2:
        if set1[i]!=set2[j]:
            s3.add(set1[i])
        else:
            pass
print(s3)

