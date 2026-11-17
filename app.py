
from database import create_table, register_user, login_user
from security import validate_username, validate_password
import getpass

create_table()

print("===== SECURE USER MANAGEMENT SYSTEM =====")

while True:

    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        try:
            validate_username(username)
            validate_password(password)

            if register_user(username, password):
                print("Registration successful!")
            else:
                print("Username already exists.")

        except ValueError as error:
            print(error)

    elif choice == "2":

        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if login_user(username, password):
            print("Login successful!")
        else:
            print("Invalid username or password.")

    elif choice == "3":

        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")
