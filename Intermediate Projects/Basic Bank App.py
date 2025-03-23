class BankAccount:
    
    def __init__(self,  account_holder_name, account_number, account_balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = account_balance

    def deposit(self, deposit_amount):
        print("-" *60)
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"${deposit_amount} was added to balance")
            print(f"💰 New Balance: ${self.balance}\n")
        else:
            print("Deposit amount must be greater than $0")
        return
    
    def withdraw(self, withdraw_amount):
        print("-" *60)
        if withdraw_amount > self.balance:
            print("❌ Insufficient Funds!")
        else:
            self.balance -= withdraw_amount
            print(f"✅ ${withdraw_amount} has been withdrawn successfully!")
            print(f"💰 New Balance: ${self.balance}\n")
        return
    
    def check_balance(self):
        print("-" *60)
        print(f"👤 Account Holder: {self.account_holder_name}")
        print(f"💰 Your balance is ${self.balance}")
