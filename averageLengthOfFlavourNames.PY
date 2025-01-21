# List of suggested ice cream flavors
ice_cream_flavors = [
    "Vanilla", "Chocolate", "Strawberry", 
    "Salted Caramel", "Matcha", "Cookies & Cream", 
    "Rainbow Sherbet", "Bubblegum", "Cotton Candy", 
    "Mango", "Pineapple-Coconut", "Key Lime Pie"
]

# Calculate the total length of all flavor names
total_length = sum(len(flavor.replace(" ", "")) for flavor in ice_cream_flavors)



# Calculate the average length of flavor names
average_length = total_length / len(ice_cream_flavors)

# Display the suggested flavors and the average length
print("Suggested Ice Cream Flavors:")
for flavor in ice_cream_flavors:
    print(f"- {flavor}")

print(f"\nAverage Length of Flavor Names: {average_length:.2f}")