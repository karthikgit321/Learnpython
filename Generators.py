#Square of numbers using Generators
'''
def square(my_nums):
    result=[]
    for i in my_nums:
        result.append(i*i)
    return result
list=([1,2,3,4,5])
sq=square(list)
print(sq)
'''

def square(my_nums):
    for i in my_nums:
        yield (i*i)


sq=square(([1,2,3,4,5]))
'''
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
'''
for i in sq:
    print (i)


