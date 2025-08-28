import random
import string

def generate_password(length=12, use_letters=True, use_numbers=True, use_symbols=True):
    # Define character sets
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    
    # Create character pool based on user preferences
    characters = ''
    if use_letters:
        characters += letters
    if use_numbers:
        characters += numbers
    if use_symbols:
        characters += symbols
        
    if not characters:
        return "Error: At least one character type must be selected!"
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to Password Generator!")
    while True:
        print("\nOptions:")
        print("1. Generate Simple Password (letters only)")
        print("2. Generate Medium Password (letters + numbers)")
        print("3. Generate Strong Password (letters + numbers + symbols)")
        print("4. Generate Custom Password")
        print("5. Exit")
        
        choice = input("\nChoose an option (1-5): ")
        
        if choice == '1':
            password = generate_password(length=8, use_numbers=False, use_symbols=False)
            print(f"Your password: {password}")
            
        elif choice == '2':
            password = generate_password(length=10, use_symbols=False)
            print(f"Your password: {password}")
            
        elif choice == '3':
            password = generate_password(length=12)
            print(f"Your password: {password}")
            
        elif choice == '4':
            try:
                length = int(input("Enter password length: "))
                use_letters = input("Include letters? (y/n): ").lower() == 'y'
                use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
                use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
                
                password = generate_password(
                    length=length,
                    use_letters=use_letters,
                    use_numbers=use_numbers,
                    use_symbols=use_symbols
                )
                print(f"Your password: {password}")
            except ValueError:
                print("Please enter a valid number for length!")
                
        elif choice == '5':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
