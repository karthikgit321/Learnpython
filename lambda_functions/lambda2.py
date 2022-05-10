
#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.

#Syntax
#filter(function, iterable)

a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd=list(filter(lambda x:x%2!=0,a))
print(odd)
even=list(filter(lambda x:x%2==0,a))
print(even)