numbers=input("Enter the list of numbers").split()
print(list)
sum_of_even=[]
sum_of_odd=[]
for i in range(0,len(numbers)):
    numbers[i]=int(numbers[i])
print(numbers)


for i in range(0,len(numbers)):
    if i%2==0:
        sum_of_even.append(numbers[i])
    else:
        sum_of_odd.append(numbers[i])
print(sum_of_odd)
print(sum_of_even)


sum_of_even=sum(sum_of_even)
print(sum_of_even)
print(type(sum_of_even))

sum_of_odd=sum(sum_of_odd)
print(sum_of_odd)

absolute_diff=abs(sum_of_odd-sum_of_even)
print(absolute_diff)
