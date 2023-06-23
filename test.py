import random
import string
import os
import time

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    os.system("toilet The Happy Train")
    time.sleep(1)
    os.system("clear")
    os.system("sl")
    print("Welcome to The Happy Train - Password Generator")
    
    while True:
        length = input("Enter the desired password length: ")
        if length.isdigit() and int(length) >= 8:
            password = generate_password(int(length))
            print(f"Generated Password: {password}")
            break
        else:
            print("Invalid input. Please enter a valid length.")

if __name__ == "__main__":
    main()
