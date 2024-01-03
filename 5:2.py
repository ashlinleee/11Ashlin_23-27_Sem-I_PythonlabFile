from bank_module import BankAccount

account = BankAccount(10000) 

print(account.check_balance())

print(account.deposit(5000))
print(account.withdraw(2000))

print(account.check_balance())
