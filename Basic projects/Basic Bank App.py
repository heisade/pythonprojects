class BankAccount:
    bank_name = "SafeTrust Bank"

    def set_account(self, account_holder, account_number, account_balance):
        self.user = account_holder
        self.account_number = account_number
        self.balance = account_balance

    def deposit(self, deposit):
        self.balance += deposit


    def withdraw(self, withdrawal):
        if withdrawal > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= withdrawal

    def get_account(self):
        return f"Bank: {account.bank_name}\nAccount Holder: {self.user}\nAccount Number: {self.account_number}\nBalance: ${self.balance}"

account = BankAccount()

account.set_account("John Doe", "12345678", 5000)
account.deposit(500)
account.withdraw(1000)
print(account.get_account())
