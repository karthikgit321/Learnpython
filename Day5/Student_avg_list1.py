students_height=input("Enter the list of students height\n").split()
print(students_height)
for i in range(0,len(students_height)):
    students_height[i]=float(students_height[i])
print(students_height)

count=0
sum=0

for element in students_height:
    count+=1
print(count)

for i in range(0,count):
    sum=sum+students_height[i]
print(sum)

Avg=round(sum/count)
print(f"The Avg height of the students is {Avg}")