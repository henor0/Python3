from abc import ABC, abstractmethod

# Abstract class (Abstraction)
class BankAccount(ABC):
    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = value

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

# Concrete class (Encapsulation and Property Decorators)
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self._interest_rate = interest_rate

    # Deposit method (Implemented)
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    # Withdraw method (Implemented)
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Insufficient balance.")

    # Additional method to calculate interest
    def calculate_interest(self):
        return self._balance * self._interest_rate

# Usage Example
try:
    account = SavingsAccount("John Doe", 1000)
    print(f"Account Owner: {account._owner}")
    print(f"Initial Balance: ${account.balance}")

    # Deposit
    account.deposit(500)
    print(f"Balance after deposit: ${account.balance}")

    # Withdraw
    account.withdraw(200)
    print(f"Balance after withdrawal: ${account.balance}")

    # Calculate Interest
    interest = account.calculate_interest()
    print(f"Interest earned: ${interest}")

    # Trying invalid deposit
    account.deposit(-100)  # This will raise an error

except ValueError as e:
    print(e)
