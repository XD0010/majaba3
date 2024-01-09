import string


def get_password_length():
    while True:
        try:
            a = int(input("How many characters do you want the password to be: "))
            if a <= 0:
                print("Please enter a positive integer for the password length.")
            else:
                return a
        except ValueError:
            print("Invalid input. Please enter a valid positive integer for the password length.")


def get_character_types():
    character_types = ""
    while not character_types:
        print("Enter the types of characters to include in the password:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Digits")
        print("4. Special characters")
        print("Type the corresponding numbers (e.g., '1' for uppercase letters, '1234' for all types).")
        character_types = input("Your choice: ")

        if any(char not in "1234" for char in character_types) or len(character_types) == 0:
            print("Invalid input. Please enter a valid combination of numbers.")
            character_types = ""

    return character_types


def generate_password(length, character_types):
    characters = ""
    if "1" in character_types:
        characters += string.ascii_uppercase
    if "2" in character_types:
        characters += string.ascii_lowercase
    if "3" in character_types:
        characters += string.digits
    if "4" in character_types:
        characters += string.punctuation

    if len(characters) == 0:
        print("Error: No character types selected. Please try again.")
        return None

    import random
    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Welcome to the Password Generator!")
    length = get_password_length()
    character_types = get_character_types()
    password = generate_password(length, character_types)

    if password:
        print("Generated Password:", password)


main()
