# Input a single character from the user
letter = input("Enter a single letter: ").lower()

# Check if the input is a valid letter
if len(letter) == 1 and letter.isalpha():
    # Check if the letter is a vowel or consonant
    if letter in "aeiou":
        print(f"'{letter}' is a vowel.")
    else:
        print(f"'{letter}' is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic letter.")