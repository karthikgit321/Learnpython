students_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

students_grades={
    "scores 91-100":"Grade=outstanding",
    "scores 81-90":"Grade=Exceeds expectation",
    "scores 71-80":"Grade=Acceptable",
    "scores 70 or lesser":"Grade=Fail"
}

for score in students_scores:
    if 90<=students_scores[score]>=100:
        print(students_grades["scores 91-100"])
    elif 81<=students_scores[score]>=90:
        print(students_grades["scores 81-90"])
    elif 71 <= students_scores[score] >= 80:
        print(students_grades["scores 71-80"])
    else:
        print(students_grades["scores 70 or lesser"])