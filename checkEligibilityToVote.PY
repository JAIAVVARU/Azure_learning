# Input the user's age
age = int(input("Enter your age: "))

# Check if the age is 18 or older
if age >=100 or age <= 0:
    print("enter valid age")
elif age >= 18:
    print("you are eligible to vote.")
else:
    print("You are not eligible to vote.")