import os

DATABASE_FILE = "database.txt"      # Remember to create a database.txt(or name it what you want to name it) file and put it in the same folder as this file and boom there you have it

# Load users from file
def load_users():
    database = {}
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if ":" in line:
                    username, password = line.split(":", 1)
                    database[username] = password
    return database

# Save users to file
def save_users(database):
    with open(DATABASE_FILE, "w") as file:
        for username, password in database.items():
            file.write(f"{username}:{password}\n")

# Register User
def register(database, username, password):
    if username in database:
        print("❌ Username already exists!")
        return database

    if not username or ":" in username:
        print("❌ Invalid username! (Cannot be empty or contain ':')")
        return database

    if not password:
        print("❌ Password cannot be empty!")
        return database

    database[username] = password
    save_users(database)
    print("✅ User registered successfully!")
    return database

# Login User
def login(database, username, password):
    if database.get(username) == password:
        print("✅ Login successful!")
    else:
        print("❌ Invalid username or password.")

# Delete Profile
def delete_profile(database, username, password):
    if database.get(username) == password:
        del database[username]
        save_users(database)
        print(f"✅ User '{username}' deleted successfully!")
    else:
        print("❌ Invalid username or password. Profile not deleted.")
    return database

# Main Program Execution
def main():
    users_db = load_users()  # Load users only once

    while True:  # Loop to allow multiple operations
        print("\n================ Welcome to the Login System! ================\n")
        user_choice = input("Enter [1] to Login\n"
                            "Enter [2] to Create a New Profile\n"
                            "Enter [3] to Delete a Profile\n"
                            "Enter [4] to Exit\n"
                            "Enter choice: ").strip()

        if user_choice == '1':
            username = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            login(users_db, username, password)

        elif user_choice == '2':
            username = input("Enter new username: ").strip()
            password = input("Enter password: ").strip()
            users_db = register(users_db, username, password)  # Update user database

        elif user_choice == '3':
            confirm = input("Are you sure you want to delete your profile? (y/n): ").strip().lower()
            if confirm == 'y':
                username = input("Enter username: ").strip()
                password = input("Enter password: ").strip()
                users_db = delete_profile(users_db, username, password)  # Update user database
            else:
                print("Profile deletion canceled.")

        elif user_choice == '4':
            print("Exiting program... 👋")
            break

        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



# Possible update: Moving from using a text file as the database and moving to useing actual database like SQLite or MySQL 
# But i need to learn flask or Django which is my choice because i want to learn it with SQL.