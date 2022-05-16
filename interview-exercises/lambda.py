# def multipliers():
#     return [lambda x : i * x for i in range(4)]
#
# print(m[2] for m in multipliers())

l1=[1,2,3]
l2=l1
l2.append(5)
print(l2)
print(l1)
print(id((l2)))
print(id(l1))

