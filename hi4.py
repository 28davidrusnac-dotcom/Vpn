def get_letter_grade(grade: int)->str:
    if grade >= 90:
        return "A"
    elif grade >=80:
        return "B"
    elif grade>=70:
        return "C"
    elif grade>=60:
        return "D"
    else:
        return "F"
    
score= int(input("enter your score"))
print(get_letter_grade(score))