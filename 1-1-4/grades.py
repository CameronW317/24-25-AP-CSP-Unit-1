grade = (int(input("Please enter the grade you got on the last test")))

if grade >= 90:
    print("A")
elif grade < 90 and grade >= 80:
    print("B")
elif grade <80 and grade >= 80:
    print("C")
elif grade <= 70 and grade >= 65:
    print("D")
else:
    print("You failed, try again next year")