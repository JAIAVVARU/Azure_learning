# Input two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Check if the second number is not zero to avoid division by zero
if num2 != 0:
    # Check divisibility
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}.")
    else:
        remainder = num1 % num2
        print(f"{num1} is not divisible by {num2}. The remainder is {remainder}.")
else:
    print("Division by zero is not allowed.")