# Input the number, start, and end of the range from the user
number = float(input("Enter the number: "))
start = float(input("Enter the start of the range: "))
end = float(input("Enter the end of the range: "))

# Check if the number is within the range
if start <= number <= end:
    print("In range")
else:
    print("Out of range")