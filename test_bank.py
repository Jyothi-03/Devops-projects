"""
Unit tests for the banking system.
"""

import unittest
from bank import Bank
from enums import AccountType


class TestBank(unittest.TestCase):
    """
    Validates core banking behavior and rules.
    """

    def setUp(self):
        self.bank = Bank()
        self.account = self.bank.open_account(
            "Test User", AccountType.SAVINGS, 500
        )

    def test_deposit(self):
        self.bank.deposit(self.account, 100)
        self.assertEqual(self.bank.accounts[self.account].balance, 600)

    def test_withdraw_min_balance_violation(self):
        self.bank.withdraw(self.account, 450)
        self.assertEqual(self.bank.accounts[self.account].balance, 500)

    def test_apply_interest(self):
        self.bank.apply_monthly_interest()
        self.assertAlmostEqual(
            self.bank.accounts[self.account].balance, 510, places=2
        )


if __name__ == "__main__":
    unittest.main()
