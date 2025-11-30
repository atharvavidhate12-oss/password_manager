from password_checker import check_password_strength
from manager import save_credentials, view_credentials

def main():
    while True:
        print("\n=== PASSWORD MANAGER ===")
        print("1. Check Password Strength")
        print("2. Save Credentials")
        print("3. View Saved Credentials")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            password = input("Enter a password to check: ")
            strength, feedback = check_password_strength(password)
            print("\nResult:", strength)
            if feedback:
                print("Suggestions:")
                for msg in feedback:
                    print("-", msg)

        elif choice == "2":
            site = input("Enter site name: ")
            username = input("Enter username: ")
            password = input("Enter password: ")

            save_credentials(site, username, password)
            print("Credentials saved securely ✔")

        elif choice == "3":
            view_credentials()

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
