class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def set_balance(self, balance):
        """Sets the balance for the account"""
        self.balance = balance

    def deposit(self, amount):
        """Adds the amount to deposited to the balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Checks that the amount to be withdrawn is greater than or equal to the balance.
        If it is, then the amount is subtracted from the balance. If not, the user is notified of insufficient funds."""
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance is ${self.balance}")
        else:
            print("Insufficient Funds")

    def get_balance(self):
        """Gets the balance of the account."""
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_holder, balance, interest_rate, months):
        # Call the constructor of the base class explicitly
        Account.__init__(self, balance, interest_rate)
        self.account_holder = account_holder
        self.months = months

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance is ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance is ${self.balance}")
        else:
            print("Insufficient Funds")

    def calculate_interest(self):
        interest_earned = float(self.balance * self.interest * self.months / 12 / 100)
        self.balance += interest_earned
        print(f"Interest earned: ${interest_earned}. New balance: ${self.balance}")
        return self.balance, interest_earned


class CdAccount(Account):
    def __init__(self, account_holder, balance, interest_rate, months):
        # Call the constructor of the base class explicitly
        Account.__init__(self, balance, interest_rate)
        self.account_holder = account_holder
        self.months = months

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New Balance is ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New Balance is ${self.balance}")
        else:
            print("Insufficient Funds")

    def calculate_interest(self):
        interest_earned = float(self.balance * self.interest * self.months / 12 / 100)
        self.balance += interest_earned
        print(f"Interest earned: ${interest_earned}. New balance: ${self.balance}")
        return self.balance, interest_earned


# Example usage
account_holder = "John Doe"
initial_balance = 1000.0
interest_rate = 5.0
months = 6

# Create instances of SavingsAccount and CdAccount
savings_account = SavingsAccount(account_holder, initial_balance, interest_rate, months)
cd_account = CdAccount(account_holder, initial_balance, interest_rate, months)

# Deposit and withdraw
savings_account.deposit(500)
savings_account.withdraw(200)

cd_account.deposit(1000)
cd_account.withdraw(500)

# Calculate interest
updated_savings_balance, interest_earned_savings = savings_account.calculate_interest()
updated_cd_balance, interest_earned_cd = cd_account.calculate_interest()

# Print results
print(f"Savings Account - Updated balance: ${updated_savings_balance}, Interest earned: ${interest_earned_savings}")
print(f"CD Account - Updated balance: ${updated_cd_balance}, Interest earned: ${interest_earned_cd}")
