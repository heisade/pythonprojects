class BankAccount:
    
    def __init__(self,  account_holder_name, account_number, account_balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = account_balance
        self.transaction = []

    def deposit(self, deposit_amount):
        print("-" *60)
        if deposit_amount > 0:
            self.balance += deposit_amount
            print(f"${deposit_amount} was added to balance")
            print(f"💰 New Balance: ${self.balance}")
            self.transaction.append(f"🟢 Deposited {deposit_amount} | New Balance: {self.balance}")
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
            print(f"💰 New Balance: ${self.balance}")
            self.transaction.append(f"🔴 Withdrawn: {withdraw_amount} | New Balance: {self.balance}")
        return
    
    def check_balance(self):
        print("-" *60)
        print(f"👤 Account Holder: {self.account_holder_name}")
        print(f"💰 Your balance is ${self.balance}")

    def transaction_history(self):
        print("-" * 60)
        if not self.transaction:
            print("📜 No transaction history available.")
            return
        print(f"📜 Transaction History:")
        for index, history in enumerate(self.transaction):
            print(f"{index+1}. {history}")

