marks = float(input("Enter your marks: "))
if marks >= 80:
    print("Your grade is A")
elif 60 <= marks <= 79:
    print("Your grade is B")
elif 40 <= marks <= 59:
    print("Your grade is C")
else:
    print("Fail")