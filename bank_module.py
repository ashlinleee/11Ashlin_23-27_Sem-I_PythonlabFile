class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        return f"Your current balance is: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. Your new balance is: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Withdrawn {amount}. Your new balance is: {self.balance}"
