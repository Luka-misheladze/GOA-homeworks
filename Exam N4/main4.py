def student_grade(grade):
    if grade >= 90:
        return("A")
    elif grade >= 80:
        return("B")
    elif grade >= 70:
        return("C")
    elif grade == 67:
        return("A+")
    elif grade == 61:
        return("A+++")
    else:
        return("F")
print(student_grade(grade=int(input("Please enter ur grade: "))))