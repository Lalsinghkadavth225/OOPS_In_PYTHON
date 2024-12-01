class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self._transaction_history = []

    # Getter for balance
    @property
    def balance(self):
        return self._balance

    # Setter for balance (we do not allow direct modification)
    @balance.setter
    def balance(self, value):
        raise ValueError("We cannot set the balance directly.")

    # Deposit method
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than 0")
        self._balance += amount
        self._transaction_history.append(f"Deposited INR {amount} Rupees")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount should be greater than 0")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._transaction_history.append(f"Withdrew INR {amount} Rupees")

    # Property for transaction history
    @property
    def transaction_history(self):
        return self._transaction_history

# Create a BankAccount object
bank_account = BankAccount("Lalsingh", 1000)

# Check balance (getter)
print(bank_account.balance)  # Output: 1000

# Deposit money
bank_account.deposit(40)
print(bank_account.balance)  # Output: 1040

# Withdraw money
bank_account.withdraw(200)
print(bank_account.balance)  # Output: 840

# Try withdrawing more than the balance
try:
    bank_account.withdraw(1000)
except ValueError as e:
    print(e)  # Output: Insufficient funds

# View transaction history
print(bank_account.transaction_history)
