# Create file to store expenses
output_file_path = "Expense Tracker.txt"
with open(output_file_path, "a") as f:
    print("File created!")


def user_balance():
        try:
            balance = int(input("Enter your balance: "))
            print(f"Your balance is {balance}")
            with open("Expense Tracker.txt", "a") as file:
                file.write(str(balance) +"\n")
        except ValueError:
             print("Invalid Input. Please enter a valid integar.")


def read_balance():
    try:
        with open("Expense Tracker.txt", "r") as file:
            balance_str = file.readline().strip()  # Read the balance as a string
            balance = int(balance_str)  # Convert the string back to an integer
            print(f"Your current balance is {balance}")
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except ValueError:
        print("File contains invalid data. Expected an integer.")


def add_balance():
    try:
        amount_added = int(input("Enter amount you want to add to your balance: "))
        try:
            with open("Expense Tracker.txt", "r") as file:
                balance_str = file.readline().strip()
                balance = int(balance_str)
                new_balance = amount_added + balance
        except FileNotFoundError:
            balance = 0

        with open("Expense Tracker.txt", 'w') as file:
                file.write(str(new_balance) + "\n")

        print(f"Amount added: {amount_added}")
        print(f"Your New balance is: {new_balance}")

    except ValueError:
         print("Invalid Input. Please enter a valid integar.")


def deduct_balance():
    try:
        amount_spent = int(input("Enter amount you want to add to your balance: "))
        try:
            with open("Expense Tracker.txt", "r") as file:
                balance_str = file.readline().strip()
                balance = int(balance_str)
                new_balance = balance - amount_spent
        except FileNotFoundError:
            balance = 0

        with open("Expense Tracker.txt", 'w') as file:
                file.write(str(new_balance) + "\n")

        print(f"Amount deducted: {amount_spent}")
        print(f"Your New balance is: {new_balance}")

    except ValueError:
         print("Invalid Input. Please enter a valid integar.")


print('===================== Expense Tracker =====================')
user_input = input("Enter [1] to create balance\n"
                   "Enter [2] to add to balance\n"
                   "Enter [3] for amount spent\n"
                   "Enter [4] to check balance\n"
                   "Enter input: ")

if user_input == '1':
    user_balance()
elif user_input == '2':
    add_balance()
elif user_input == '3':
     deduct_balance()
elif user_input == '4':
     read_balance()
else:
     print("Invalid input. Please enter a valid input")