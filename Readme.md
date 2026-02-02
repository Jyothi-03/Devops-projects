# Banking System – Python

## Overview
This project is a simple banking system built using Python and object-oriented programming principles.  
It supports multiple account types, transaction processing, and maintains a complete transaction history for each account.

---

## Features
- Create and manage bank accounts
- Support for **Checking** and **Savings** accounts
- Deposit, withdraw, and transfer funds
- Enforce account-specific rules:
  - Checking: no minimum balance, first 10 transactions per month free, $2.50 fee afterward
  - Savings: minimum balance $100, max 5 withdrawals per month, earns 2% monthly interest
- Maintain complete transaction history
- Generate monthly statements
- Reject invalid transactions
- Unit tests included

---

## Account Types

### Checking Account
- No minimum balance
- First 10 transactions per month are free
- $2.50 fee after 10 transactions

### Savings Account
- Minimum balance of $100
- Maximum 5 withdrawals per month
- Earns 2% monthly interest

---

## Project Structure

```
assessment-1/
├── account.py           # Account logic and rules
├── bank.py              # Bank operations and coordination
├── transaction.py       # Transaction record model
├── enums.py             # Enums for account and transaction types
├── demo.py              # Sample execution with multiple transactions
├── test_bank.py          # Unit tests
└── README.md

```
---

## How to Run

### Run the demo

The demo script creates multiple accounts and performs successful and failed transactions to demonstrate system behavior.

`python demo.py`

### Run unit tests

Unit tests are written using Python’s built-in unittest framework.

`python -m unittest test_bank.py`

## Example Output

```
kappaganthubrahmarambhikajyothi ~ python demo.py                 
Statement for a65f84e4-2b2b-4cfb-b939-80a8bd5abcc7
----------------------------------------
2026-02-02 22:30:34.764301 | TRANSFER | Amount: $300 | 1000 → 700 | SUCCESS
2026-02-02 22:30:34.764309 | DEPOSIT | Amount: $50 | 700 → 750 | SUCCESS
2026-02-02 22:30:34.764313 | WITHDRAWAL | Amount: $100 | 750 → 650 | SUCCESS
2026-02-02 22:30:34.764318 | WITHDRAWAL | Amount: $100 | 650 → 550 | SUCCESS
2026-02-02 22:30:34.764322 | WITHDRAWAL | Amount: $100 | 550 → 450 | SUCCESS
2026-02-02 22:30:34.764327 | WITHDRAWAL | Amount: $100 | 450 → 350 | SUCCESS
2026-02-02 22:30:34.764331 | WITHDRAWAL | Amount: $100 | 350 → 250 | SUCCESS
2026-02-02 22:30:34.764336 | WITHDRAWAL | Amount: $100 | 250 → 250 | FAILED | Reason: Maximum withdrawals exceeded
2026-02-02 22:30:34.764341 | DEPOSIT | Amount: $5.0 | 250.0 → 255.0 | SUCCESS
Ending Balance: $255.00

```


---

## Testing Objectives Checklist

- [x] Object-oriented design (Account, Transaction, Bank classes)  
- [x] Collection management (accounts map, transactionHistory list)  
- [x] Transaction validation (negative balance prevention, account rules enforcement)  
- [x] State management (monthly transaction counts, savings interest, account balances)

---

## Assignment Requirements Checklist

- [x] Implement **Account**, **Transaction**, and **Bank** classes  
- [x] Support account types: CHECKING and SAVINGS  
- [x] Transaction types: DEPOSIT, WITHDRAWAL, TRANSFER  
- [x] Record transactions with:
  - transactionId
  - timestamp
  - type
  - amount
  - balanceBefore
  - balanceAfter
  - status (SUCCESS/FAILED with reason)
- [x] Reject transactions violating account rules (negative balance, withdrawal limits, etc.)  
- [x] Apply monthly interest for savings accounts  
- [x] Generate monthly statements showing transactions and ending balance  
- [x] Demonstrate with at least 4 accounts and 20 transactions (including failed attempts)  
- [x] Unit tests for all core methods  
- [x] README includes setup, sample input/output, and assumptions  

---

## Assumptions

- Checking accounts have no minimum balance  
- Savings accounts must maintain a minimum balance of $100  
- First 10 transactions per month in checking accounts are free; additional transactions incur $2.50 fee  
- Savings accounts allow a maximum of 5 withdrawals per month  
- Monthly interest (2%) is applied only to savings accounts at the end of each month  
- Transactions that would result in negative balance are rejected  
- Transaction amounts must be numeric and positive  
- Transaction history includes all attempts (success and failed)  

---

## Author
Developed and submitted as part of the Intuit Software Engineer build-up challenge to demonstrate object-oriented design, validation logic, and testing practices.