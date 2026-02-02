"""
Bank module.

Acts as the orchestrator for all account operations.
Handles validation, transaction creation, and state updates.
"""

import uuid
from enums import AccountType, TransactionType, TransactionStatus
from account import Account
from transaction import Transaction


class Bank:
    """
    Bank manages all accounts and their transactions.
    """

    def __init__(self):
        self.accounts = {}

    def open_account(self, customer_name, account_type, initial_deposit):
        """
        Opens a new account and returns the account number.
        """
        account_number = str(uuid.uuid4())
        self.accounts[account_number] = Account(
            account_number, account_type, initial_deposit
        )
        return account_number

    def close_account(self, account_number):
        """
        Closes an account only if its balance is zero.
        """
        account = self._get_account(account_number)
        if account.balance != 0:
            raise ValueError("Account balance must be zero to close")
        del self.accounts[account_number]

    def deposit(self, account_number, amount):
        """
        Deposits funds into an account.
        """
        account = self._get_account(account_number)
        before = account.balance

        if amount <= 0:
            self._record_failed(account, TransactionType.DEPOSIT, amount, "Invalid deposit amount")
            return

        account.balance += amount
        self._apply_checking_fee(account)
        self._record_success(account, TransactionType.DEPOSIT, amount, before)

    def withdraw(self, account_number, amount):
        """
        Withdraws funds after validating account rules.
        """
        account = self._get_account(account_number)
        before = account.balance

        allowed, reason = account.can_withdraw(amount)
        if not allowed:
            self._record_failed(account, TransactionType.WITHDRAWAL, amount, reason)
            return

        account.balance -= amount
        account.monthly_withdrawal_count += 1
        self._apply_checking_fee(account)
        self._record_success(account, TransactionType.WITHDRAWAL, amount, before)

    def transfer(self, from_account, to_account, amount):
        """
        Transfers funds between two accounts.
        """
        source = self._get_account(from_account)
        target = self._get_account(to_account)

        before = source.balance
        allowed, reason = source.can_withdraw(amount)

        if not allowed:
            self._record_failed(source, TransactionType.TRANSFER, amount, reason)
            return

        source.balance -= amount
        target.balance += amount
        self._record_success(source, TransactionType.TRANSFER, amount, before)

    def apply_monthly_interest(self):
        """
        Applies interest and resets monthly counters.
        """
        for account in self.accounts.values():
            interest = account.apply_interest()
            if interest > 0:
                account.transaction_history.append(
                    Transaction(
                        TransactionType.DEPOSIT,
                        interest,
                        account.balance - interest,
                        account.balance,
                        TransactionStatus.SUCCESS
                    )
                )
            account.reset_monthly_counters()

    def generate_monthly_statement(self, account_number):
        """
        Generates a full monthly statement.
        """
        account = self._get_account(account_number)
        lines = [f"Statement for {account.account_number}", "-" * 40]
        for tx in account.transaction_history:
            lines.append(str(tx))
        lines.append(f"Ending Balance: ${account.balance:.2f}")
        return "\n".join(lines)

    # ---------- Internal Helpers ----------

    def _apply_checking_fee(self, account):
        """
        Applies checking account transaction fees.
        """
        account.monthly_transaction_count += 1
        if (
            account.account_type == AccountType.CHECKING
            and account.monthly_transaction_count > Account.CHECKING_FREE_TX
        ):
            account.balance -= Account.CHECKING_FEE

    def _record_success(self, account, tx_type, amount, before):
        """
        Records a successful transaction.
        """
        account.transaction_history.append(
            Transaction(
                tx_type,
                amount,
                before,
                account.balance,
                TransactionStatus.SUCCESS
            )
        )

    def _record_failed(self, account, tx_type, amount, reason):
        """
        Records a failed transaction.
        """
        account.transaction_history.append(
            Transaction(
                tx_type,
                amount,
                account.balance,
                account.balance,
                TransactionStatus.FAILED,
                reason
            )
        )

    def _get_account(self, account_number):
        """
        Retrieves an account or raises an error.
        """
        if account_number not in self.accounts:
            raise ValueError("Account not found")
        return self.accounts[account_number]
