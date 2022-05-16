#syntax:
#lambda arguments : expression
'''
a=1
b=2
c=3

x=lambda a,b,c :a+b+c
print(x(1,5,6))

ages = [13, 90, 17, 59, 21, 60, 5]

adults = list(filter(lambda age: age > 18, ages))

print(adults)


add=lambda a : a+15
print((add(int(input("enter the number")))))

mul=lambda x,y :x*y
print(mul(10,20))

multiply=lambda a,b : a*b
a=int(input("enter the num"))
b=int(input("entere the num"))
print(multiply(a,b))
'''
def f(n):
    return lambda x:x*n
res=f(2)
print(res(15))