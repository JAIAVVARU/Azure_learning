def check_number():
    try:
        # Take input from the user
        number = float(input("Enter a number: "))

        # Check the number's classification
        if number > 0:
            print("Positive")
        elif number < 0:
            print("Negative")
        else:
            print("Zero")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Run the function
check_number()