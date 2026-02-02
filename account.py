"""
Account module.

Defines the Account class and encapsulates
account-specific rules and state.
"""

from enums import AccountType


class Account:
    """
    Represents a bank account.

    Handles:
    - Account balance
    - Transaction history
    - Monthly transaction tracking
    - Account-type-specific rules
    """

    # Checking account rules
    CHECKING_FREE_TX = 10
    CHECKING_FEE = 2.50

    # Savings account rules
    SAVINGS_MIN_BALANCE = 100
    SAVINGS_MAX_WITHDRAWALS = 5
    SAVINGS_INTEREST_RATE = 0.02

    def __init__(self, account_number, account_type, initial_balance):
        """
        Initializes an account with required state.
        """
        self.account_number = account_number
        self.account_type = account_type
        self.balance = initial_balance

        # State management
        self.transaction_history = []
        self.monthly_transaction_count = 0
        self.monthly_withdrawal_count = 0

    def can_withdraw(self, amount):
        """
        Validates whether a withdrawal or transfer is allowed.

        Returns:
            (bool, reason)
        """
        if amount <= 0:
            return False, "Invalid amount"

        if self.account_type == AccountType.SAVINGS:
            if self.monthly_withdrawal_count >= self.SAVINGS_MAX_WITHDRAWALS:
                return False, "Maximum withdrawals exceeded"
            if self.balance - amount < self.SAVINGS_MIN_BALANCE:
                return False, "Minimum balance violation"

        if self.balance - amount < 0:
            return False, "Insufficient funds"

        return True, None

    def apply_interest(self):
        """
        Applies monthly interest for savings accounts only.
        """
        if self.account_type == AccountType.SAVINGS:
            interest = self.balance * self.SAVINGS_INTEREST_RATE
            self.balance += interest
            return interest
        return 0

    def reset_monthly_counters(self):
        """
        Resets monthly counters at the end of the billing cycle.
        """
        self.monthly_transaction_count = 0
        self.monthly_withdrawal_count = 0
