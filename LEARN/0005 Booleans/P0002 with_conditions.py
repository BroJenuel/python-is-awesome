passingMark = 90

enterMarks = float(input("Enter Mark: "))

if enterMarks > 100:
    print("Oops, that mark is too high")
elif enterMarks >= passingMark:
    print("Your Eligible")
else:
    print("Your not Eligible")
