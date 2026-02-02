"""
Transaction module.

Defines the Transaction class, which represents
an immutable audit record of a banking operation.
"""

from datetime import datetime
import uuid


class Transaction:
    """
    Represents a single transaction performed on an account.

    Each transaction records:
    - Unique ID
    - Timestamp
    - Type (deposit, withdrawal, transfer)
    - Amount
    - Balance before and after the transaction
    - Status (success or failure)
    - Optional failure reason
    """

    def __init__(
        self,
        transaction_type,
        amount,
        balance_before,
        balance_after,
        status,
        reason=None
    ):
        self.transaction_id = str(uuid.uuid4())
        self.timestamp = datetime.now()
        self.type = transaction_type
        self.amount = amount
        self.balance_before = balance_before
        self.balance_after = balance_after
        self.status = status
        self.reason = reason

    def __str__(self):
        """
        Human-readable transaction format for statements.
        """
        base = (
            f"{self.timestamp} | {self.type.value} | "
            f"Amount: ${self.amount} | "
            f"{self.balance_before} → {self.balance_after} | "
            f"{self.status.value}"
        )
        return base if not self.reason else f"{base} | Reason: {self.reason}"
