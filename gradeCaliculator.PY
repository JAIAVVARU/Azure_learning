

# Input the score from the user
score = float(input("enter the score(0 to 100): "))

#check the range and assign the grade

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
elif 50 <= score < 60:
    grade = "E"
else:
    grade = "Invalid score" 

# Output the grade
print(f"the grade is: {grade}")