import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to The Happy Train - Password Generator")

    while True:
        length = input("Enter the desired password length (8 or more characters): ")
        if length.isdigit() and int(length) >= 8:
            break
        print("Invalid input. Please enter a valid length.")

    password = generate_password(int(length))
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
