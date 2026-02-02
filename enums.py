"""
Enums used across the banking system to ensure
type safety and avoid magic strings.
"""

from enum import Enum


class AccountType(Enum):
    """
    Supported account types.
    """
    CHECKING = "CHECKING"
    SAVINGS = "SAVINGS"


class TransactionType(Enum):
    """
    Supported transaction types.
    """
    DEPOSIT = "DEPOSIT"
    WITHDRAWAL = "WITHDRAWAL"
    TRANSFER = "TRANSFER"


class TransactionStatus(Enum):
    """
    Possible transaction outcomes.
    """
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
