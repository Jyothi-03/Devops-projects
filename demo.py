from bank import Bank
from enums import AccountType
from datetime import datetime, timedelta

bank = Bank()

# Create accounts
a1 = bank.open_account("Alice", AccountType.CHECKING, 500)
a2 = bank.open_account("Bob", AccountType.SAVINGS, 1000)
a3 = bank.open_account("Charlie", AccountType.CHECKING, 300)
a4 = bank.open_account("Diana", AccountType.SAVINGS, 150)

# Transactions (success + failures)
bank.deposit(a1, 200)
bank.withdraw(a1, 100)
bank.withdraw(a4, 100)         # ❌ min balance violation
bank.transfer(a2, a1, 300)
bank.transfer(a3, a1, 500)    # ❌ insufficient funds
bank.deposit(a2, 50)
bank.withdraw(a2, 100)
bank.withdraw(a2, 100)
bank.withdraw(a2, 100)
bank.withdraw(a2, 100)
bank.withdraw(a2, 100)
bank.withdraw(a2, 100)        # ❌ exceeds withdrawal limit

# Apply interest
bank.apply_monthly_interest()

print(bank.generate_monthly_statement(a2))
