students_score=input("Enter the list of students scores\n").split()
print(students_score)
for i in range(0,len(students_score)):
    students_score[i]=int(students_score[i])
print(students_score)

highest_score=0
for score in students_score:
    if score>highest_score:
        highest_score=score
print("The highest score is ",highest_score)

print(min(students_score))